"""
Exercise

Write a program that:
○ Input: name and year of birth.
○ Output: a string that “I am ... and I am ... years old.”
"""
import datetime


def age(yearofbirth):
  todo='''get age of yearofbirth
  currentyear - yearofbirth
  '''
  currentyear = datetime.datetime.now().year
  return currentyear - yearofbirth

def run(name, yearofbirth):
  todo=122
  print(f'I am {name} and I am {age(yearofbirth)} year(s) old.')

run(name='Dinh Thi Thao', yearofbirth=2001)
