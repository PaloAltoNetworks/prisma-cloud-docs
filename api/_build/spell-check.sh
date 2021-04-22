#!/bin/bash

# Enable common error handling options.
#set -o errexit
set -o nounset
set -o pipefail

# https://stackoverflow.com/questions/592620/how-can-i-check-if-a-program-exists-from-a-bash-script
if ! command -v mdspell &> /dev/null
then
    echo "mdspell could not be found"
    exit
fi

# https://stackoverflow.com/questions/43707685/set-u-nounset-vs-checking-whether-i-have-arguments
if (( $# >= 1 )); then
  doc_dir="$1"
else
  doc_dir="../descriptions"
fi

# https://stackoverflow.com/questions/23356779/how-can-i-store-the-find-command-results-as-an-array-in-bash
input='*.md'
array=()
while IFS=  read -r -d $'\0'; do
  array+=("$REPLY")
done < <(find "${doc_dir}" -name "${input}" -print0)

count="${#array[*]}"
if [[ count -eq 0 ]]; then
  echo "No markdown files found"
  exit 1
else
  echo "Files to spell check:"
  echo "${#array[*]}"
fi

for i in "${array[@]}"; do
   mdspell "-r" "-n" "-a" "--en-us" "${i}"
done
