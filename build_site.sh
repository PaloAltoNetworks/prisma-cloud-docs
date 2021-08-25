#!/bin/bash
#
# This script builds the Prisma Cloud Compute static doc site.
#

declare -r latest="compute_edition_21_04"

clear_output_dir() {
  # Delete all files in the output dir, except the .git dir.
  glob="$output_dir""/*"
  glob_expansion=($glob)
  for p in "${glob_expansion[@]}"; do
    rm -r "$p"
  done
}

echo "Building static site..."
if [ "$1" != "" ]; then
  doc_dir=$(dirname "$1")
else
  doc_dir="."
fi

work_dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
output_dir="$work_dir""/output"

srcAdmin="$doc_dir""/admin_guide"
srcTroubleshooting="$doc_dir""/troubleshooting"
srcGovernment="$doc_dir""/government"

# Delete previous build.
if [ -d "$output_dir" ]
then
  rm -rf "$output_dir"
fi

# Delete Python virtualenv.
pyenv uninstall -f build_site_env

# Create output dir.
mkdir "$output_dir"

# Set up Python env.
echo "Set up Python env"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
pyenv virtualenv 3.7.4 build_site_env
pyenv activate build_site_env
pip install -r requirements.txt

# Initialize a git repo.
cd "$output_dir"
git init
git config user.name "build"
git config user.email "<>"
cd "$work_dir"

#
# ADMIN GUIDE (self-hosted)
#

# Copy admin guide files into place.
# https://stackoverflow.com/questions/3643848/copy-files-from-one-directory-into-an-existing-directory
echo "Copy admin guide files"
cp -R "$srcAdmin""/." "$output_dir"
cp -R "$work_dir""/_files/." "$output_dir"

# Rename topic map file.
mv "$output_dir""/_topic_map_compute_edition.yml" "$output_dir""/_topic_map.yml"

# Fix up doc tree source files.
python "_build/format_fixup.py" "$output_dir""/_topic_map.yml"

# Commit files.
cd "$output_dir"
git add -A
git commit -q -m "Commit admin guide (Compute Edition)"

#
# ADMIN GUIDE (SaaS)
#

# The second distro needs its own index file in the main branch.
cp "index-main.html" "index-main2.html"
git add -A
git commit -q -m "Commit index file for SaaS book"

# Create a branch
git checkout -b pcee

# Delete all files.
clear_output_dir

# Copy admin guide files into place.
echo "Copy admin guide files"
cd "$work_dir"
cp -R "$srcAdmin""/." "$output_dir"
cp -R "$work_dir""/_files/." "$output_dir"

# Rename topic map file.  
mv "$output_dir""/_topic_map_prisma_cloud.yml" "$output_dir""/_topic_map.yml"

# Fix up doc tree source files.
python "_build/format_fixup.py" "$output_dir""/_topic_map.yml"

# Commit files.
echo "Commit SaaS files"
cd "$output_dir"
git add -A
git commit -q -m "Commit admin guide (SaaS)"


#
# TROUBLESHOOTING
#

# Create a branch.
git checkout -b troubleshooting

# Delete all files.
clear_output_dir

# Copy files into place.
echo "Copy Troubleshooting files"
cd "$work_dir"
cp -R "$work_dir""/_files/." "$output_dir"
cp -R "$srcTroubleshooting""/." "$output_dir"

# Fix adoc source files (not required for the Troubleshooting content).
#python format_fixup.py "$output_dir""_topic_map.yml"

# Commit files.
echo "Commit Troubleshooting files"
cd "$output_dir"
git add -A
git commit -q -m "Commit Troubleshooting"

#
# GOVERNMENT
#

# Create a branch.
git checkout -b government

# Delete all files.
clear_output_dir

# Copy files into place.
echo "Copy Government files"
cd "$work_dir"
cp -R "$work_dir""/_files/." "$output_dir"
cp -R "$srcGovernment""/." "$output_dir"

# Fix adoc source files
#python "_build/format_fixup.py" "$output_dir""/_topic_map.yml"

# Commit files.
echo "Commit Government files"
cd "$output_dir"
git add -A
git commit -q -m "Commit Government"


# Generate the static site.
# asciibinder_pan package -l debug
echo "Generate static site"
git checkout master
asciibinder_pan package

cd "$output_dir""/_package/main"
cp -R "../main2/enterprise_edition" "."

# Point the compute_edition directory to latest
#ln -s "${latest}" "compute_edition"
cp -a "${latest}" "compute_edition"
