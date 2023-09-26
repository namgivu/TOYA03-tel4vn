"""
0123456789012345678901
PythonForDevops
       PythonForDevops
PythonForDevops.......
.......PythonForDevops       
"""

s='PythonForDevops'
print(s.ljust(22))
print(s.rjust(22))

print(s.ljust(22, '.'))
print(s.rjust(22, '.'))

print('\n---\n')

print(f'{s:<22}')
print(f'{s:>22}')
print(f'{s:.<22}')
print(f'{s:.>22}')

print(f'{s.ljust(22,".")}')
