"""
3. Reading template file and fill in
Given a template text file “template.txt” (on classroom assignment)
Ask user to input:
- Name
- A place
- An action
Replace inputs in the template file with NAME, PLACE and ACTION. Then
write the output to a text file “output.txt”

template.txt:
NAME walkes to the PLACE and then they ACTION.
NAME asks another person to ACTION too.
"""

NAME   = 'Nam'
PLACE  = 'Van Hanh Mall'
ACTION = 'go shopping'

# doc temp template.txt luu vao bien :template_str
from pathlib import Path
THIS_DIR   = Path(__file__).parent
template_f = str(THIS_DIR/'template.txt')

f = open(template_f)
template_str = f.read()
f.close()


# thuchien .replace() de dien vao cac bien
print(template_str)
o = template_str.replace('NAME',   NAME)
o =            o.replace('PLACE',  PLACE)
o =            o.replace('ACTION', ACTION)
print(o)


# xuat ra output.txt
output_f = str(THIS_DIR/'output.txt')

fo = open(output_f, 'w')
fo.write(o)
fo.close()
