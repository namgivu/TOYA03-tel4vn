#region run df -h
import sys

try:    file_system = sys.argv[1]
except: file_system = None
# except: file_system = 'udev'

import subprocess
output = subprocess.run(f'''df -h | grep -E "Size|{file_system}" | awk '{{print $2, $4}}' ''', capture_output=True, shell=True)
print(f'{output.returncode=}')
print('\noutput.stderr.decode()\n', output.stderr.decode())
print('\noutput.stdout.decode()\n', output.stdout.decode())
#endregion run df -h

s = output.stdout.decode()
'''
754M 752M
3,7G 3,6G
5,0M 5,0M
3,7G 3,7G
754M 754M
'''
size  = s.split('\n')[1].split(' ')[0]
avail = s.split('\n')[1].split(' ')[1]
print(f'{size=:>} {avail=:>}')
