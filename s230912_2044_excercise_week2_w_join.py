"""
Given a list of things:
○ things = ['pen', 'ruler', 'wallet', 'phone']
○ Write a function return the string contains all items, seperate by comma (,), but the 'and' before the last item.
"""
things = ['pen', 'ruler', 'wallet', 'phone']
# things = ['pen', 'ruler', 'wallet', 'phone', '0', '1', '22']

things_without_lastitem = things[0:len(things)-2 +1]

s = ', '.join(things_without_lastitem)
s = s + ' and ' + things[len(things)-1]
print(s)
