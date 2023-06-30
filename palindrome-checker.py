str=input()
str_2=str.lower()
str_3=str_2[::-1]
if str_2==str_3:
  print('palindrome')
else:
  print('not palindrome')