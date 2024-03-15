# Created by Mr. ROPON POV
import os

def rename_files(directory, replace_with):
  """Renames all files in the specified directory with user-defined format,
  excluding Python files ('.py').

  Args:
    directory: The directory path containing the files to rename.
    replace_with: The string to use as the base name in the new filenames.
  """
  counter = 1
  for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
      base, extension = os.path.splitext(filename)
      if extension.lower() != '.py': 
        new_filename = f"{replace_with}_{counter:02d}{extension}"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        print(f"Renamed: {filename} -> {new_filename}")

script_dir = os.path.dirname(os.path.realpath(__file__))

replace_with = input("What do you want to rename the files to? (without extension): ")

rename_files(script_dir, replace_with)

print(f"\nFiles successfully renamed in '{script_dir}' (excluding Python files)!")
