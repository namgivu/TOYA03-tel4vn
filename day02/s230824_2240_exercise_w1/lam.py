"""
ref https://drive.google.com/drive/u/1/folders/1joIRyyF-X_cl3eawCjvODvbbeOM9C7ni

Write a program that:
○ Input: name and year of birth.
○ Output: a string that “I am ... and I am ... years old.”
"""

# Input: name and year of birth.
name = input('What is your name? ')
year = input('What year was you born? ')

# “I am ... and I am ... years old.”
def tinhtuoi(namsinh):
    """tinh tuoi tu nam sinh"""
    #      nam hientai                  - namsinh
    return datetime.datetime.now().year - namsinh

#region age
# age = 2023 - int(year)  # wrong age if currentyear <> 2023

import datetime
current_year = datetime.datetime.now().year
age          = current_year - int(year)  # wrong age if currentyear <> 2023
#endregion age

print(f'I am {name} and I am {age} years old')
