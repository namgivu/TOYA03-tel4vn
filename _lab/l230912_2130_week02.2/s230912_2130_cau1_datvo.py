"""
Parsing uri:
Giving url = "https://tel4vn.edu.vn/course/python-for-devops/"

Split the string to get:
a. The protocol "https"
b. 3 parts of domain ["tel4vn", "edu", "vn"]
c. 2 parts of path ["course", "python-for-devops"]
"""

'''by Dat VO'''
url = "https://tel4vn.edu.vn/course/python-for-devops/"
url_split = url.split('/')

# Cau a
# protocol = url_split[0][0:len(url_split[0]) - 2 + 1]
protocol = url_split[0][ :-1]
# protocol = url_split[0][0:-1]
# protocol = url_split[0][0:len(url_split)-1]

# Cau b
domain       = url_split[2]  # tel4vn.edu.vn
domain_split = domain.split('.')

# Cau c
# path = url_split[len(url_split) - 3:len(url_split) - 2 + 1]
path = url_split[3:4 +1]

print(f'   {url_split=}')
print(f'    {protocol=}')
print(f'{domain_split=}')
print(f'        {path=}')
