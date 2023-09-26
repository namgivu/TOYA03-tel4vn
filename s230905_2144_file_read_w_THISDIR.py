import os

THIS_FILE = __file__
THIS_DIR  = os.path.dirname(__file__)  # dir of THIS_FILE
print(f'THIS_DIR={THIS_DIR}')
print(f'{THIS_DIR=}')

f  = open(f'{THIS_DIR}/input.txt')  #NOTE must cd to same folder where input.txt is stored
fc = f.read()  # fc aka filecontent
f.close()

print(fc)
