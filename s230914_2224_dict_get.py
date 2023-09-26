d = {
  'a':122,
  'b':333,
}
print(d['a'])
print(d['b'])
# print(d['c'])     # will raise error as key :c notexist
print(d.get('c') )  # will NOT raise error as key :c notexist
print(d.get('c', 'valwhennotexist') )
