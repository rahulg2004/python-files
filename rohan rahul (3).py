'''PROGRAM 1
a=int(input("enter no.a"))
b=int(input("enter no.b"))
c=int(input("enter no.c"))
disc=b**2-4*a*c
root1=(b+disc**0.5)/2*a
root2=(b-disc**0.5)/2*a
if disc==0:
    print("both same roots exist",root1,root2)
elif disc>0:
    print("unique roots exist",root1,root2)
else:
    print("roots does not exist")'''


''' Program 2
a=int(input("enter no. you want to check"))
if a%2==0:
    print("number",a,"is even")
else:
    print("number",a,"is odd")'''

'''
a=int(input("enter no.a"))
total=0
for i in range(1,a+1):
    total+=i
print("sum of natural no.till",a,"is",total)'''



'''program3
a=int(input("enter no.a"))
for i in range(2,a):
    if a%i==0:
        print(a,"is not prime no.")
        break
    else:
        print(a,"is prime no.")
        break



a=int(input("enter no. you want to check"))

for i in range(2,a+1):
    c=0
    for j in range(2,i):
        b=i%j
        if b==0:
            c+=1
    if c==0:
        print(i)'''
'''N=int(input("enter the no."))

def nextprime(num):
    while True:
        num+=1
        for i in range(2,num):
            if num%i==0:
                break
            else:
                return num
def prime(N):
    num,count=1,1
    while count<=N:
        num=nextprime(num)
        print(num)
        count+=1
prime(N)'''
    








    


''''PROGRAM3
n=int(input("enter no."))

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end='')
    for k in range(1,2*i):
        print("*",end="")

    print()

for i in range(n,0,-1):
    for j in range((3*n)-i):
        print(" ",end='')
    for k in range(1,2*i):
        print("*",end="")

    print()'''








'''char=input("enter the character")
if char.isalpha()==True:
    print("CHARACTER YOU ENTERED IS A LETTER")
    if char.isupper()==True:
        print(" &  CHARACTER YOU ENTERED IS IN UPPERCASE")
    else:
        print(" & CHARACTER YOU ENTERED IS IN LOWER CASE")
elif char.isdigit()==True:
    print("CHARACTER YOU ENTERED IS A NUMERIC DIGIT")
    d={"0":"zero","1":"ONE","2":"TWO","3":"THREE","4":"FOUR","5":"FIVE","6":"SIX","7":"SEVEN","8":"EIGHT","9":"NINE"}
    print(d.get(char))
    
else:
    print("CHARACTER YOU ENTERED IS A SPECIAL SYMBOL")'''



'''var=input("ENTER THE CHARACTER")
def countfre():
    fre=input("ENTER THE CHARACTER YOU WANT TO CHECK FRECUENCY")
    a=var.count(fre)
    print("FRECUENCY OF ",fre,"in ",var,"is",a)
def toreplace():
    rep=input("ENTER THE CHARACTER YOU WANT TO REPLACE")
    torep=input("ENTER THE CHARACTER REPLACE CHARACTER WITH")
    b=var.replace(rep,torep)
    print(b)
def removefirst():
    rem=input("ENTER THE CHARACTER YOU WANT TO REMOVE ITS FIRST OCCURENCE")
    c=var.replace(rem,'',1)
    print(c)
def removeall():
    arem=input("ENTER THE CHARACTER YOU WANT TO REMOVE ITS all OCCURENCE")
    d=var.replace(arem,'')
    print(d)
countfre()
toreplace()
removefirst()
removeall()'''




'''def replace1():
    n=int(input("enter no. of letters you have  to replace"))
    st1=input("enter first string")
    st2=input("enter second string")
    im=st1[0:n]
    tw=st2[0:n]
    new1=st1.replace(im,tw)
    print("THE FIRST STRING IS",new1)
    new2=st2.replace(tw,im)
    print("THE SECOND STRING IS",new2)
replace1()'''



'''st1=input("enter the string")
st2=input("enter the string")
a=len(st1)
b=len(st2)
for j in range(0,b):
    for i in range(0,a):
        if st1[i]==st2[j]:
            print("Same at index of a&b respectively:-",i,",",j)'''
        
'''program 8'''
'''def listcube():
    num=int(input("enter length of list"))
    lis=[]
    for i in range(1,num+1):
        if i%2==0:
            a=i**3
            lis.append(a)
    print(lis)
listcube()'''

'''def listcomp():
    num=int(input("enter length of list"))
    lis=[x**3 for x in range(1,num+1)
         if x%2==0]
    print(lis)
listcomp()'''


'''program 11'''
'''def dictcube():
    num=int(input("enter length of dictionary"))
    dicti={x:x**3 for x in range(1,num+1)}
    print(dicti)
dictcube()'''

'''program 12 '''
'''def half():
    t1=(1,2,5,7,9,2,4,6,8,10)
    list1 =list(t1)
    l= int(len(list1)//2)
    a=list1[0:l]
    b=list1[l:]
    print(a)
    print(b)
half()
'''


'''def con():
    t1=(1,2,5,7,9,2,4,6,8,10)
    list1=list(t1)
    list2=[]
    for i in list1:
        if i%2==0:
            list2.append(i)
    print(tuple(list2))
con()
'''

'''def conf():
    t1=(1,2,5,7,9,2,4,6,8,10)
    t2=(11,13,15)
    list1 = list(t1)
    list2 = list(t2)
    list3 = list1 + list2
    tup=tuple(list3)
    print(tup)
conf()'''

def minmax():
    t1=(1,2,5,7,9,2,4,6,8,10)
    t2=(11,13,15)
    list1 = list(t1)
    list2 = list(t2)
    list3 = list1 + list2
    a = max(list3)
    b = min(list3)
    print("THE MAXIMUM VALUE : ", a)
    print("THE MINIMUM VALUE : ", b)

minmax()
        
    
    
    




    


















