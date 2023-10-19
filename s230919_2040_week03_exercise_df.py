#region run df -h
import sys

try:    file_system = sys.argv[1]
except: file_system = None
# except: file_system = 'udev'

import subprocess
output = subprocess.run(f'df -h | grep -E "Size|{file_system}" ', capture_output=True, shell=True)
#      =           .run                                         ,                    , shell=True to use pipe | in command

print(f'{output.returncode=}')
print('\noutput.stderr.decode()\n', output.stderr.decode())
print('\noutput.stdout.decode()\n', output.stdout.decode())
#endregion run df -h

#region get :size :avail
s = output.stdout.decode().split('\n')[1]

#    Filesystem      Size      Used     Avail  Use% Mounted on
# s = 'udev            3,7G      0        3,7G   0%   /dev'
# s = 'tmpfs           754M      2,2M     752M   1%   /run'
#    [^ ]+[ ]+       [^ ]+ [ ]+[^ ]+[ ]+[^ ]+

import re
m = re.findall('[^ ]+[ ]+([^ ]+)[ ]+[^ ]+[ ]+([^ ]+).+', s)
size  = m[0][0]
avail = m[0][1]
print(f'{size=} {avail=} ')
#endregion get :size :avail

'''
--- sample run+output
sudo python3 main.py udev
size='3,7G' avail='3,7G' 

sudo python3 main.py tmpfs
size='754M' avail='752M' 
'''