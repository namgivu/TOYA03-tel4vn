from pathlib import Path


THIS_FILE = Path(__file__)
THIS_DIR  = THIS_FILE.parent

print(f'''
THIS_FILE={THIS_FILE}
THIS_DIR={THIS_DIR}
''')

f = open( THIS_DIR/'input.txt' )
s = f.read()
f.close()
print(s)

# prepare output dir
output_f = THIS_DIR/'output'/'230907.txt'
Path.mkdir(output_f.parent)

fo = open(output_f, 'w')
fo.write(s)
fo.close()
