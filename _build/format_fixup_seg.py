import argparse
import pathlib
import re
import shutil
import sys
import tempfile
import yaml

# Record that holds all command line params.
#  topic_map_path   - Path to topic map.
#  topic_map_yaml   - Topic map YAML.
#  input_dir        - Path to top of output dir.
class Config:
  pass

def fix_doc_tree(config):
  """
  Constructs a directory that holds all converted files, graphics, and the topic_map.
  """
  # Fix up each ADOC file in the topic map.
  print('Fixing up adoc source files')

  for chapter in config.topic_map_yaml:
    directory = pathlib.Path(config.input_dir) / pathlib.Path(chapter['Dir'])
    walk_segment(config, chapter, directory)


def walk_segment(config, segment, directory, depth=1):

  for article in segment['Topics']:
    if 'Topics' in article:
      nested_dir = pathlib.Path(directory) / pathlib.Path(article['Dir'])
      walk_segment(config, article, nested_dir, depth+1)
    else:
      src_file = pathlib.Path(directory).joinpath(article['File'])
      src_file = src_file.with_suffix('.adoc')
      insert_header(config, article['Name'], src_file)
      rename_lvl2_heading(src_file)
      sed_inplace(src_file, r'^== ', '= ')

      include_path = src_file.relative_to(get_output_path(src_file))
      include_path = include_path.parent
      sed_inplace(src_file, r'^include::', f'include::{include_path}/')

  
def get_output_path(path):
  '''
  Get the path to the output dir.
  '''
  p = path.resolve()
  for rel_path in path.parents:
    if 'output' in rel_path.parts[-1]:
      return rel_path
  return ''


def insert_header(config, title, src_file):

  with src_file.open(mode='r') as f:
    save = f.read()

  with src_file.open(mode='w') as f:
    f.write(f'= {title}\n')
    f.write(":nofooter:\n")
    f.write(":source-highlighter: highlightjs\n")

  with src_file.open(mode='a') as f:
    f.write(save)


def rename_lvl2_heading(filename):
  '''
  Each article has one level 2 heading (to support conversion to DITA).

  == Heading

  Rename it to "Overview":

  == Overview

  '''
  # For efficiency, precompile the passed regular expression.
  pattern_compiled = re.compile('== ')

  # For portability, NamedTemporaryFile() defaults to mode "w+b" (i.e., binary
  # writing with updating). This is usually a good thing. In this case,
  # however, binary writing imposes non-trivial encoding constraints trivially
  # resolved by switching to text writing. Let's do that.
  with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
    with filename.open() as f:
      for line in f:
        if pattern_compiled.match(line):
          tmp_file.write("")
        else:
          tmp_file.write(line)

  # Overwrite the original file with the munged temporary file in a
  # manner preserving file attributes (e.g., permissions).
  shutil.copystat(filename, tmp_file.name)
  shutil.move(tmp_file.name, filename)


def sed_inplace(filename, pattern, repl):
  '''
  Perform the pure-Python equivalent of in-place `sed` substitution: e.g.,
  `sed -i -e 's/'${pattern}'/'${repl}' "${filename}"`.

  See: https://stackoverflow.com/questions/4427542/how-to-do-sed-like-text-replace-with-python
  '''
  # For efficiency, precompile the passed regular expression.
  pattern_compiled = re.compile(pattern)

  # For portability, NamedTemporaryFile() defaults to mode "w+b" (i.e., binary
  # writing with updating). This is usually a good thing. In this case,
  # however, binary writing imposes non-trivial encoding constraints trivially
  # resolved by switching to text writing. Let's do that.
  with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp_file:
    with filename.open() as f:
      for line in f:
        tmp_file.write(pattern_compiled.sub(repl, line))

  # Overwrite the original file with the munged temporary file in a
  # manner preserving file attributes (e.g., permissions).
  shutil.copystat(filename, tmp_file.name)
  shutil.move(tmp_file.name, filename)


def validate_file_path(file_path):
  """
  Validate the input path is a directory that contains a _topic_map.yml file.
  """
  path = pathlib.Path(file_path)

  # Check if file exists in the file system at the specified path
  if path.exists():
    return True
  else:
    print(f'Cannot find {file_path}')
    sys.exit(1)


def main():
  """
  """
  parser = argparse.ArgumentParser(description='Fix up source adoc files for nicer formatting in the static site')
  parser.add_argument('topic_map', type=str, help='Path to _topic_map.yml')
  args = parser.parse_args()

  # FIX: The Config class should have methods to parse and save config options.
  config = Config()

  if validate_file_path(args.topic_map):
    config.topic_map_path = pathlib.Path(args.topic_map)
  config.input_dir = config.topic_map_path.parent

  # Open and read the topic map. If the file cannot be parsed,
  # exit the program and return 1.
  with config.topic_map_path.open(mode='r') as stream:
    try:
      config.topic_map_yaml = list(yaml.full_load_all(stream))
    except yaml.YAMLError as e:
      print(f'Error: Invalid YAML in _topic_map.yml: {e}')
      sys.exit(1)

  fix_doc_tree(config)

  print('OK')


if __name__ == '__main__':
  main()
