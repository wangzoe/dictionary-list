#dictionary & list

from random import randint
contact=[]
contact_info={}
for i in range(0,3):
    contact_info['name']=input('enter your name: ')
    contact_info['age']=eval(input('enter your age: '))
    contact_info['code']=randint(0,10)
    contact.append(contact_info)
    print(contact)

print('Please enter your certification information as request')
name=input('First name: ')
age=eval(input('Age: '))

for contact_info in contact[:]:
    if name.lower()==contact_info['name']:
        n=True
    else:
        n=False
    if contact_info['age']==age:
        a=True
    else:
        a=False

if n==True and a==True:
    print('Your code is '+str(contact_info['code']))
else:
    print("We couldn't find your information.")       
