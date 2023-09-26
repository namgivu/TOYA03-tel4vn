"""
Reading logs file
Given a nginx “sample.log” files (on classroom assignment ie in LAB folder, file TOYA03-week2.2_hw.zip )

Log format is:
<ip> - - <date-time> <request> <http code> <body size> <host> <user-agent>
eg
<ip>          - - <date-time>                  <request>              <http code> <body size> <host>                <user-agent>
66.249.65.159 - - [05/Oct/2022:19:10:38 +0600] "GET /sample HTTP/1.1" 404         177         "https://example.com" "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
172.25.65.3   - - [06/Oct/2022:19:11:24 +0600] "GET /sample HTTP/1.1" 200         4223        "https://example.com" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"

Write a python function to read from this log file and print out this
information:
- Total of success (2xx) and failed (4xx, 5xx) requests.
- Output the client ip that has the most 4xx requests.
"""


#region cau 1
'''
cau 1
- Total of success (2xx) and failed (4xx, 5xx) requests.
'''

# read sample.log file
from pathlib import Path
THIS_FILE = Path(__file__)
THIS_DIR  = THIS_FILE.parent
log_f     = THIS_DIR/'sample.log'

f=open(log_f)
lines = f.readlines()
f.close()

lines = [i.strip() for i in lines  if i]

success_count = 0
failed_count  = 0

for line in lines:
  print(f'{line=}')
  if not line: continue  # skip the empty/invalid log line

  line_split = line.split('"', )

  print(line_split[2])                        # <http code> <body size>  # eg  403 5316
  print(line_split[2].strip())                #                          # eg 403 5316
  print(line_split[2].strip().split(' ')[0])  #                          # eg 403
  http_code   = line_split[2].strip().split(' ')[0]  # 403
  http_code_0 = http_code[0]                         # 4

  '''
  success (2xx)
  failed (4xx, 5xx)
  '''
  if http_code_0 == '2':  # success (2xx)
    success_count  = success_count + 1
    # success_count += 1

  elif http_code_0 == '4' or http_code_0 == '5' :  # failed (4xx, 5xx)
    failed_count += 1

  print()

print(f'{success_count=}')

# print('failed_count='+str(failed_count))
print(f'{failed_count=}')
#endregion cau 1


print('\n---\n')

#region cau 2
'''
- Output the client ip that has the most 4xx requests.

use :dict
ip : http_code

notallow :dict
(ip, http_code)
filter by http_code=4xx
sort by ip 

eg
ip1 4xx
ip1 4xx
ip1 4xx

ip2 4xx
ip2 4xx
...

count by ip
ip1 count_ip1
ip2 count_ip2
...

'''
ip_httpcode_list = []
for line in lines:
  print(f'{line=}')
  if not line: continue  # skip the empty/invalid log line

  line_split = line.split('"', )

  # get http_code 4xx
  print(line_split[2])                        # <http code> <body size>  # eg  403 5316
  print(line_split[2].strip())                #                          # eg 403 5316
  print(line_split[2].strip().split(' ')[0])  #                          # eg 403
  http_code   = line_split[2].strip().split(' ')[0]  # 403
  http_code_0 = http_code[0]                         # 4
  print(f'{http_code_0=}')

  # get ip
  print(line_split[0])                # eg 47.29.201.179 - - [23/Oct/2022:14:17:10 +0
  print(line_split[0].split(' ')[0])  # eg 47.29.201.179
  ip = line_split[0].split(' ')[0]

  ip_httpcode_list.append(
    (ip, http_code_0)
  )

print(f'{ip_httpcode_list=}')  # eg [('66.249.65.159', '4'), ('172.25.65.3', '2'), ('185.19.60.62', '2'), ('47.29.201.179', '5'), ('66.249.65.159', '4'), ('47.29.201.179', '2'), ('47.29.201.179', '2'), ('66.249.65.159', '4'), ('47.29.201.179', '5'), ('66.249.65.159', '4'), ('47.29.201.179', '2')]

# filter by http_code=4xx
ip_httpcode_list = [i for i in ip_httpcode_list if i[1]=='4' ]
print(f'{ip_httpcode_list=}')  # eg [('66.249.65.159', '4'), ('66.249.65.159', '4'), ('66.249.65.159', '4'), ('66.249.65.159', '4')]

# sort by ip
ip_httpcode_list.sort()
print(f'{ip_httpcode_list=}')  # eg [('1.22.333.123', '4'), ('1.22.333.123', '4'), ('1.22.333.123', '4'), ('1.22.333.123', '4'), ('1.22.333.123', '4'), ('1.22.333.123', '4'), ('66.249.65.159', '4'), ('66.249.65.159', '4'), ('66.249.65.159', '4'), ('66.249.65.159', '4'), ('66.249.65.159', '4')]

ip_count = 1
ip_count_list = []
for idx,e in enumerate(ip_httpcode_list):  # e aka element/item
  if idx == len(ip_httpcode_list)-1:
    i_next = None
  else:
    i_next = ip_httpcode_list[idx+1]

  ip      = e[0]
  ip_next = i_next[0] if i_next else None

  if ip   == ip_next:
    # still same ip --> count it
    ip_count += 1

  elif ip != ip_next:
    ip_count_list.append(
      (ip_count, ip)
    )

    # start counting w/ new ip
    ip_count = 1
    ip = ip_next

print(f'{ip_count_list=}')  # eg ip_count_list=[(6, '1.22.333.123'), (5, '66.249.65.159')]
ip_count_list.sort(reverse=True)
ip_count_max = ip_count_list[0]

print(f'{ip_count_max=}')  # eg ip_count_max=(6, '1.22.333.123')
ip_w_4xx_maxcount = ip_count_max[1]
print(f'{ip_w_4xx_maxcount=}')  # eg ip_count_max=(6, '1.22.333.123')
#endregion cau 2
