"""
2. Reading logs file
Given a nginx “sample.log” files (on classroom assignment)
Log format is:
<ip> - - <date-time> <request> <http code> <body size> <host> <user-agent>
Write a python function to read from this log file and print out this
information:
- Total of success (2xx) and failed (4xx, 5xx) requests.
- Output the client ip that has the most 4xx requests.

--- eg
1.22.333.123  - - [23/Oct/2022:13:17:10 +0000] "GET /sample HTTP/1.1" 403 5316 "https://example.com" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36" "2.75"
66.249.65.159 - - [23/Oct/2022:13:17:10 +0000] "GET /sample HTTP/1.1" 403 5316 "https://example.com" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36" "2.75"

--- thinking
ip 2
ip 4
ip 5
...

"""
import re
import json
from pathlib import Path


THIS_DIR = Path(__file__).parent
log_f    = THIS_DIR/'sample.log'

f = open(log_f) ; lines = f.readlines() ; f.close()
lines = [l.strip() for l in lines]

'''
cook below data from :lines
ip 2
ip 4
ip 5
...

'''
ip_c_list = []  # c aka http_code
for line in lines:
  m  = re.findall(r'(.*) - - (.*)', line)
  ip = m[0][0]

  m2 = re.findall(r'(.*)"(.*)" (\d\d\d).*', m[0][1])
  http_code      = m2[0][2]
  http_code_idx0 = http_code[0]

  ip_c_list.append({'ip':ip, 'c': http_code_idx0})

print('\n---\n')
print(json.dumps(ip_c_list, indent=2))

count_2xx     = 0
count_4xx_5xx = 0
for d in ip_c_list:
  print(d)
  print(d['c'])
  if d['c'] == '2':         count_2xx     += 1
  if d['c'] in ['4', '5'] : count_4xx_5xx += 1
print(f'{count_2xx=}')
print(f'{count_4xx_5xx=}')

print('\n---\n')
'''
gom ip co c=4 vao :count_4_d
ip1: dembaonhieulan4
ip2: dembaonhieulan4
...

'''
count_4_d = {}
for d in ip_c_list:
  c  = d['c']
  ip = d['ip']

  if c == '4':
    # d['ip'] aka :ip la ungvien can gom
    if   ip not in count_4_d: count_4_d[ip]  =  1
    elif ip     in count_4_d: count_4_d[ip] +=  1
print(count_4_d)

maxontop = sorted(count_4_d.items(), key=lambda i: i[1], reverse=True)
print(maxontop[0])
maxcount_4xx    = maxontop[0][1]
maxcount_4xx_ip = maxontop[0][0]
print(f'ip={maxcount_4xx_ip} has max 4xx in {maxcount_4xx} times')
