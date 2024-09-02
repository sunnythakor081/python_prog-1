d={'sandip':'17-11-2003',
  'hemal':'02-12-2004',
  'sunny':'10-07-2001',
  'anis':'13-05-1999',
  'nithsh':'23-08-2005'}

dob=input("Enter any month:")

for key,i in d.items():

    if(i[3:5]==dob):
      print('Date of birth:  {}:{}'.format(key,i))
    else:
      dob=0
if(dob==0):
   print("data not found")
