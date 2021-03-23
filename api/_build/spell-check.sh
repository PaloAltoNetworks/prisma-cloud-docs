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

# https://stackoverflow.com/questions/23356779/how-can-i-store-the-find-command-results-as-an-array-in-bash
input='*.md'
array=()
while IFS=  read -r -d $'\0'; do
  array+=("$REPLY")
done < <(find "../descriptions" -name "${input}" -print0)

echo "Files to spell check:"
echo "${#array[*]}"

for i in "${array[@]}"; do
   mdspell "-r" "-n" "-a" "--en-us" "${i}"
done
