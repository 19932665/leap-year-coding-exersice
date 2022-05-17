
leap_year=(int(input("which year do you want to check ")))
if leap_year % 4 == 0 :
  if leap_year % 100 == 0:
    if leap_year % 400 == 0:
       print("leap year")
    else:
     print("not a leap year")
  else:
   print("leap year")
else:
  print("not a leap year")
