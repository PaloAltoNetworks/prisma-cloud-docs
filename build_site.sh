#!/bin/bash
#
# This script builds the Prisma Cloud Compute static doc site.
#

show_help() {
  echo "
Usage: build_site.sh [OPTIONS] [DOC_SOURCE]

build_site.sh builds the Prisma Cloud Compute static site.

OPTIONS:
  -r                            Populate release notes with CDN download links


DOC_SOURCE:
  path                          Path to AsciiDoctor doc source from the twistlock/docs repo
                                (default: current working directory)
"
}

clear_output_dir() {
  # Delete all files in the output dir, except the .git dir.
  glob="$output_dir""/*"
  glob_expansion=($glob)
  for p in "${glob_expansion[@]}"; do
    rm -r "$p"
  done
}

optspec=":r"
while getopts "${optspec}" opt; do
  case "${opt}" in
    r )
      publish_cdn_links=true
      ;;
    \?)
      show_help
      exit
      ;;
  esac
done
shift "$((OPTIND-1))"

echo "Building static site..."
if [ "$1" != "" ]; then
  doc_dir=$(dirname "$1")
else
  doc_dir="."
fi

work_dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
output_dir="$work_dir""/output"

srcAdmin="$doc_dir""/admin_guide"
srcRN="$doc_dir""/rn"
srcOps="$doc_dir""/ops_guide"
srcRefArch="$doc_dir""/ref_arch"
srcHistorical="$doc_dir""/historical"
srcTroubleshooting="$doc_dir""/troubleshooting"
srcSegmentGuide="$doc_dir""/segment_guide"

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

# Rename topic map file.  
mv "$output_dir""/_topic_map_prisma_cloud.yml" "$output_dir""/_topic_map.yml"

# Commit files.
echo "Commit SaaS files"
git add -A
git commit -q -m "Commit admin guide (SaaS)"

#
# RELEASE NOTES
#

# Create a branch.
git checkout -b rn

# Delete all files.
clear_output_dir

# Copy files into place.
echo "Copy release notes files"
cd "$work_dir"
cp -R "$work_dir""/_files/." "$output_dir"
cp -R "$srcRN""/." "$output_dir"
mv "$output_dir""/_topic_map_static_site.yml" "$output_dir""/_topic_map.yml"

# Fix adoc source files
python "_build/format_fixup.py" "$output_dir""/_topic_map.yml"
if [ "$publish_cdn_links" == "true" ]; then
  python rn_details.py "$output_dir""/_topic_map.yml" "../../release_info.yml"
fi

# Commit files.
echo "Commit release files"
cd "$output_dir"
git add -A
git commit -q -m "Commit release notes"

#
# OPS GUIDE
#

# Create a branch.
git checkout -b ops

# Delete all files.
clear_output_dir

# Copy files into place.
echo "Copy Ops Guide files"
cd "$work_dir"
cp -R "$work_dir""/_files/." "$output_dir"
cp -R "$srcOps""/." "$output_dir"

# Fix adoc source files
python "_build/format_fixup.py" "$output_dir""/_topic_map.yml"

# Commit files.
echo "Commit Ops Guide files"
cd "$output_dir"
git add -A
git commit -q -m "Commit Ops Guide"

#
# REFERENCE ARCHITECTURE
#

# Create a branch.
git checkout -b ref_arch

# Delete all files.
clear_output_dir

# Copy files into place.
echo "Copy Ref Arch files"
cd "$work_dir"
cp -R "$work_dir""/_files/." "$output_dir"
cp -R "$srcRefArch""/." "$output_dir"

# Fix adoc source files
python "_build/format_fixup.py" "$output_dir""/_topic_map.yml"

# Commit files.
echo "Commit Ref Arch files"
cd "$output_dir"
git add -A
git commit -q -m "Commit Ref Arch"

#
# HISTORICAL
#

# Create a branch.
git checkout -b historical

# Delete all files.
clear_output_dir

# Copy files into place.
echo "Copy Historical files"
cd "$work_dir"
cp -R "$work_dir""/_files/." "$output_dir"
cp -R "$srcHistorical""/." "$output_dir"

# Fix adoc source files
python "_build/format_fixup.py" "$output_dir""/_topic_map.yml"

# Commit files.
echo "Commit Historical files"
cd "$output_dir"
git add -A
git commit -q -m "Commit Historical"

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

# SEGMENT GUIDE
#

# Create a branch.
git checkout -b segment

# Delete all files.
clear_output_dir

# Copy files into place.
echo "Copy Segment Guide files from ${work_dir} to ${output_dir}"
cd "$work_dir"
cp -R "$work_dir""/_files/." "$output_dir"
cp -R "$srcSegmentGuide""/." "$output_dir"
gsed -i -e '/\-\-\-/{n;n;n;n;N;d}' ${output_dir}/_topic_map.yml &&
gsed -i -e '/Name: Deploy Defenders/{n;n;n;N;d}' ${output_dir}/_topic_map.yml &&
gsed -i -e 's/\.png/\.svg/g' ${output_dir}/concepts/namespaces.adoc &&
gsed -i -e 's/image::oidc-auth-app\.png\[]/\[%interactive]\nimage::oidc-auth-app\.svg\[]/g' ${output_dir}/secure/secure-oidc.adoc &&
# Fix adoc source files
python "_build/format_fixup_seg.py" "$output_dir""/_topic_map.yml"

# Commit files.
echo "Commit Segment Guide files"
cd "$output_dir"
git add -A
git commit -q -m "Commit Segment Guide"

# Generate the static site.
# asciibinder_pan package -l debug
echo "Generate static site"
git checkout master
asciibinder_pan package

cd "$output_dir""/_package/main"
cp -R "../main2/enterprise_edition" "."

