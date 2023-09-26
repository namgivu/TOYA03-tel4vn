"""
Write a program with following requirements:
- Walk through current dir and all sub-dirs.
- Print files in each directory, including, file path and file size.
- Edit all text files to print number of line at the start of each line in file.
"""
import  os


for (dirpath, dirnames, filenames) in os.walk('./LAB'):
  print(f'I am at {dirpath}:')
  for f in filenames:
    st = os.stat(f'{dirpath}/{f}')
    size = st.st_size
    print(f' File: {f} - size: {size}B')

    # read file
    o = open(f'{dirpath}/{f}')
    st_list = o.readlines()
    o.close()

    # write file
    ow = open(f'{dirpath}/{f}_output.txt','w')
    for i,st in enumerate(st_list):
      ow.write(f'{i}: {st}')
    ow.close()
