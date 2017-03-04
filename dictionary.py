#dictionary & list

from random import randint
info1={}
info2={}
info3={}
contact=[info1,info2,info3]

for i in range(0,3):
    contact[i]['name']=input('enter your name: ')
    contact[i]['age']=eval(input('enter your age: '))
    contact[i]['code']=randint(0,10)
    print(contact[i])
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
