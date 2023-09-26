# generate 1000 names male/female
import random
from random import randint

from vn_fullname_generator import generator


s_list = ''
for i in range(10000):
  #region phone number
  '''ref https://github.com/hohuuhau/seedUserAndPhoneVietnamese/blob/master/fakePhone.py#L6C1-L14C26'''
  def rand_phonenumber():
    listPhoneStart = [
      '086','096','097','098','032','033','034','035','036','037','038','039','090','093','091','094','083','084','085',
    ]
    start = random.choice(listPhoneStart)

    #random 7 number from 0000000 to 9999999
    end = random.randint(0000000, 9999999)

    phone = start + str(end)
    return phone
  phone = rand_phonenumber()
  #endregion phone number

  #region name
  gender = randint(0,1)
  name   = generator.generate(gender)
  #endregion name

  s       = f'{i:>04} {"M" if gender==1 else "F"} {phone:>10} {name}'
  s_list += s + '\n'

###

# output to file
THIS_FILE = __file__
THIS_DIR  = os.path.dirname(__file__)  # dir of THIS_FILE

f = open(f'{THIS_DIR}/output.txt', 'w')
f.write(s_list)
f.close()
