"""
2. Reading logs file
Given a nginx “sample.log” files (on classroom assignment)
Log format is:
<ip> - - <date-time> <request> <http code> <body size> <host> <user-agent>
Write a python function to read from this log file and print out this
information:
- Total of success (2xx) and failed (4xx, 5xx) requests.
- Output the client ip that has the most 4xx requests.

1.22.333.123  - - [23/Oct/2022:13:17:10 +0000] "GET /sample HTTP/1.1" 403 5316 "https://example.com" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36" "2.75"
66.249.65.159 - - [23/Oct/2022:13:17:10 +0000] "GET /sample HTTP/1.1" 403 5316 "https://example.com" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36" "2.75"
"""
import re
import json
from pathlib import Path


def regex_review():
  print('\n---\n')
  s = '122'
  m = re.findall(r'122', s)
  print(m)

  print('\n---\n')
  # =            r aka rawtext
  m = re.findall(r'122.*', '122')     ; print(True if m else False, m)
  m = re.findall(r'122.*', '122 333') ; print(True if m else False, m)

  print('\n---\n')
  m = re.findall(r'122(.*)', '122 333') ; print(True if m else False, m)

def regex_rehersal():
  # =   .findall                 ,    <ip>         - - <date-time>                  <request>              <http code> <body size> <host>                <user-agent>
  m = re.findall(r'(.*) - - (.*)', '''1.22.333.123 - - [23/Oct/2022:13:17:10 +0000] "GET /sample HTTP/1.1" 403         5316        "https://example.com" "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36" "2.75"''')
  print(json.dumps(m, indent=2) )
  print(m[0][0])
  print(m[0][1])
  ip = m[0][0]

  print('\n---\n')
  m2 = re.findall(r'(.*)"(.*)" (\d\d\d).*', m[0][1])
  print(json.dumps(m2, indent=2) )
  print(m2[0][2])
  http_code = m2[0][2]

THIS_DIR = Path(__file__).parent
log_f    = THIS_DIR/'sample.log'

f = open(log_f) ; lines = f.readlines() ; f.close()
lines = [l.strip() for l in lines]

ip_httpcode_d__list = []
for line in lines:
  # print()
  # print(line)

  m  = re.findall(r'(.*) - - (.*)', line)
  ip = m[0][0]

  m2 = re.findall(r'(.*)"(.*)" (\d\d\d).*', m[0][1])
  http_code = m2[0][2]

  print(f'{ip=:<13} {http_code_idx0=:<13}')

  d = {
    'ip'             : ip,
    'http_code'      : http_code,
    'http_code_idx0' : http_code_idx0[0],
  }
  # print(d)

  ip_httpcode_d__list.append(d)

print('\n---\n')
# print(json.dumps(ip_httpcode_d__list, indent=2) )
print(ip_httpcode_d__list)

print('\n---\n')
'''Total of success (2xx) and failed (4xx, 5xx) requests. '''
count_2xx     = 0
count_4xx_5xx = 0
for d in ip_httpcode_d__list:
  # print(d['http_code_idx0'])

  if d['http_code_idx0'] == '2':        count_2xx     = count_2xx     + 1
  if d['http_code_idx0'] in ['4', '5']: count_4xx_5xx = count_4xx_5xx + 1
print(f'{count_2xx=}')
print(f'{count_4xx_5xx=}')

print('\n---\n')
'''Output the client ip that has the most 4xx requests.'''
httpcode_iplist_d = {}
for d in ip_httpcode_d__list:
  print(d)

  http_code_idx0 = d['http_code_idx0']
  ip             = d['ip']

  chuaco_http_code = httpcode_iplist_d.get(http_code_idx0) is None
  daco_http_code   = httpcode_iplist_d.get(http_code_idx0) is not None
  # daco_http_code = not chuaco_http_code

  if chuaco_http_code: httpcode_iplist_d[http_code_idx0]  = [ip]
  elif daco_http_code: httpcode_iplist_d[http_code_idx0] += [ip]
print(json.dumps(httpcode_iplist_d, indent=2) )
print(f"{httpcode_iplist_d['4']=}")
ip_w_4xx__list = httpcode_iplist_d['4']

count_d={}
for ip in ip_w_4xx__list:
  # print(ip)
  if   ip in     count_d: count_d[ip] += 1
  elif ip not in count_d: count_d[ip]  = 1
print(count_d)

countmax = -1
ipmax    = None
for k,v in count_d.items():
  # print()
  # print(k)
  # print(v)

  ip    = k
  count = v
  if count > countmax:
    countmax = count
    ipmax    = ip
print(f'{ipmax=:<11} {countmax=}')
