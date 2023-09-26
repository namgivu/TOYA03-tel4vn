f  = open('./input.txt')  #NOTE must cd to same folder where input.txt is stored
fc = f.read()  # fc aka filecontent
f.close()

print(fc)


print('---')


with open('./input.txt') as f: 
  fc = f.read()

print(fc)
