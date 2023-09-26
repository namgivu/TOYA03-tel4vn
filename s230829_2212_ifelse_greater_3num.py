"""
max_3num(i1,i2,i3)

00 use max_2num()
                    max12 = max_2num(i1, i2)
  max123 = max_2num(max12, i3)

01 if elif else bw. i1 i2 i3
  if i1 < i2:  # i2 is max candidate

     if   i2 < i3: return i3
     else        : return i2

  else:        # i1 is max candidate

     if   i1 < i3: return i3
     else        : return i1

let's code 01
"""



def max_3num(i1, i2, i3):
  if i1 < i2:
    #region i2 is max candidate
    if i2 < i3: r=i3
    else:       r=i2
    #endregion i2 is max candidate
  else:
    #region i1 is max candidate
    if i1 < i3: r=i3
    else:       r=i1
    #endregion i1 is max candidate

  return r


i1=1;   i2=22; i3=333 ; print( f'max of {i1:<4}, {i2:<4}, {i3:<4} is {max_3num(i1,i2,i3)}' )
i1=333; i2=22; i3=1   ; print( f'max of {i1:<4}, {i2:<4}, {i3:<4} is {max_3num(i1,i2,i3)}' )
i1=22;  i2=1;  i3=333 ; print( f'max of {i1:<4}, {i2:<4}, {i3:<4} is {max_3num(i1,i2,i3)}' )
