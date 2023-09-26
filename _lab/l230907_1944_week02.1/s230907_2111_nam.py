"""
Write a program with following requirements:
- Walk through current dir and all sub-dirs.
- Print files in each directory, including, file path and file size.
- Edit all text files to print number of line at the start of each line in file.
"""
import os
from pathlib import Path


THIS_FILE = Path(__file__)
THIS_DIR  = THIS_FILE.parent

walk_d = THIS_DIR/'LAB'
for dirpath, dirnames, filenames in os.walk( str(walk_d) ):
  print(f'I am at {dirpath}:')
  for filename in filenames:
    # print file info
    filename_p = Path(f'{dirpath}/{filename}')
    f_size = filename_p.stat().st_size
    print(f'''  File: {filename} - size {f_size}B''')

    # add linenumber
    f = open( str(filename_p) )
    lines = f.readlines()
    f.close()

    lines = [
      f'{i}: {line}'
      for i,line in enumerate(lines)
    ]

    fo = open( str(filename_p)+'.output.txt', 'w' )
    fo.write(
      ''.join(lines)
    )
    fo.close()
