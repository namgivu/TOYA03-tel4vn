import json


person_d_Nam = {
  'name': 'Nam',
  'year': 1982,
}
print(person_d_Nam)

person_d_Thanh       = {'name': 'Thanh',       'year': 1982}
person_d_Han         = {'name': 'Han',         'year': 2016}
person_d_Oppenheimer = {'name': 'Oppenheimer', 'year': 1904}

person_list = [
  person_d_Nam,
  person_d_Thanh,
  person_d_Han,
  person_d_Oppenheimer,
]

print(json.dumps(person_list, indent=2) )

print('\n---\n')

people_list = [
  {'name': 'Nam',         'year': 1982},  # 0
  {'name': 'Thanh',       'year': 1982},  # 1
  {'name': 'Han',         'year': 2016},  # 2
  {'name': 'Oppenheimer', 'year': 1904},  # 3
]
print(json.dumps(people_list, indent=2) )

print('\n---\n')

print(person_d_Nam['name'])
print(person_d_Nam['year'])
print(people_list[0])
print(people_list[0]['name'])
print(people_list[0]['year'])

print('\n---\n')
# print(person_d_Nam['namee'])  # will raise error
print(person_d_Nam.get('namee'))
print(person_d_Nam.get('namee', 'valuewhenkeynotvalid'))

print('\n---\n')
print(person_d_Nam)

person_d_Nam['newkey'] = 'somevalue'
print(person_d_Nam)

print('\n---\n')
d = {}
d['ip0'] = 'httpcode0' ; print(d)
d['ip1'] = 'httpcode1' ; print(d)
d['ip2'] = 'httpcode2' ; print(d)
