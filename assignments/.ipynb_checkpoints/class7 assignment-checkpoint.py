#!/usr/bin/env python
# coding: utf-8

# # Assignment
# * create list of dictionary with (name,id,user,password,email,phone)
# * create program where user can login with user/email/phone but password must be same
# 

# In[15]:


data = [{'id':1,'name':"adil maqsood",'u':'adil','email': 'adilmaqsood@gmail.com','phone': '09233312345' ,'p':'123'},
       {'id':2,'name':"waleed khan",'u':'waleed','email': 'waleedkhan@gmail.com','phone': '092333123', 'p':'123'},
       {'id':3, "name":"Muhammad rohaib",'u':'rohaib','email': 'muhammadrohaib@gmail.com','phone': '0923331234','p':'123'}]

user = input("Enter user Name")
email = input("enter your email")
phone = input("enter your phone number")
pas = input("Password")

for d in data:
    if d['u'] == user or d['p'] == pas or d['email'] == email or d['phone'] == phone :
        print(d)
        break
else:
    print("Invalid User or Password")


# In[14]:


data = [{'id':1,'name':"adil maqsood",'u':'adil','email': 'adilmaqsood@gmail.com','phone': '09233312345' ,'p':'123'},
       {'id':2,'name':"waleed khan",'u':'waleed','email': 'waleedkhan@gmail.com','phone': '09233312345', 'p':'123'},
       {'id':3, "name":"Muhammad rohaib",'u':'rohaib','email': 'muhammadrohaib@gmail.com','phone': '09233312345','p':'123'}]

user = input("Enter user Name")
mail = input("enter your email")
phone = input("enter your phone number")
pas = input("Password")

for d in data:
    if d['u'] == user and d['p'] == pas and d['email'] == mail and d['phone'] == phone :
        print(d)
        break
else:
    print("Invalid User or Password")


# # Create Table
# 
#  1.pass argument1 2 to n table will be generated
#  
#  2.pass argument2 range of each table 1 to n
# 
# * argument1 = 3
# * agrument2 = 5

# In[30]:


table = int(input("Enter a number: "))

for i in range(1,4):
    print(f"{table} X {i} = {table*i}")


# In[31]:


table = int(input("Enter a number: "))

for i in range(1,4):
    print(f"{table} X {i} = {table*i}")


# In[29]:


table = int(input("Enter a number : "))

for i in range(1,6):
    print(f"{table} X {i} = {table*i}")


# In[28]:


table = int(input("enter a number : "))

for i in range (1,6):
    print (f"{table} x {i} = {table*i}")


# In[ ]:




