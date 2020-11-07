#Hands on Python for Beginners

#add$subtract
a = 5
num = 5
b = int(num)
c = a-b
c
4==4
4>5
4!=6
4>=4

#string addition
s1="Hello"
s2="Daksh"
s1+" "+s2

s="total no. of states in India is"
num=29
s+" "+str(num)

#practice dictionary
friends={"yash":8053271543 ,"dev": 8053915518,"vishesh": 9868763487,"baxi": 9887765430}
friends["daksh"]=9812553979
del friends["daksh"]
for key in d:
    print("key :",key,"value : ",friends[key])
#or
for k,v in friends.items(): 
    print("key :",key,"value",v)

#STRING

"""1. Create a string variable to store this text Earth revolves around the sun,
  a. Print substring “revolves”
  b. Print substring “sun” using negative index
2. Create a string variable to store this text Earth revolves around the “sun” and print it
3. Create three string variables with values “I love eating“, “veggies”, “fruits”
  a. Print “I love eating veggies and fruits” (Hint: Use + operator)
  b. Create fourth variable to store number of fruits you eat everyday. Say for example you eat 2 fruits everyday, in that case print “I love eating 2 fruits everyday”"""

text=("Earth Revolves around the sun")
text[6:14]
text[-3:]
#try some random stuff
text[-1] 
text[6:]
text[:6]

text1=' Earth revolves around the “sun” '
text1

a='I love eating ' 
b=' veggies '
c= ' fruits everyday '
e=2 
a+b+'and '+str(e)+c

#LIST

#Let us say your expense for every month are listed below,
"""January - 2200
February - 2350
 March - 2600
 April - 2130
 May - 2190
Create a list to store these monthly expenses and using that find out,
a. In Feb, how many dollars you spent extra compare to January?
b. Find out your total expense in first quarter (first three months) of the year.
c. Find out if you spent exactly 2000 dollars in any month
d. June month just finished and your expense is 1980 dollar. Add this item to our
monthly expense list
e. You returned an item that you bought in a month of April and got a refund of
200$. Make a correction to your monthly expense list based on this"""

months=["january","feb","march","april","may"]
exp=[2200,2350,2600,2130,2190]
total=months+exp
exp[1]-exp[0]
exp[1]+exp[2]+exp[3]
2000 in exp
exp.append(2000)
months.append("june")
exp[3]=exp[3]-200
exp[3]

#IF STATEMENT
"""check whether if odd or even"""
num=input("enter a number :")
num=int(num)
if num%2==0:
    print('even')
else:
    print('odd')

"""1. Write a program that uses following list of cities per country,
usa = [ “atlanta”, “new york”, “chicago”, “baltimore”]
uk = [“london”, “bristol”, “cambridge”]
india = [“mumbai”,”delhi”, “banglore”]
a. Write a program that asks user to enter a city name and it should tell you which
country it belongs to
b. Write a program that asks user to enter two cities and tell you if they both are in
same country or not"""

usa = [ "atlanta", "new york", "chicago", "baltimore"]
uk = ["london", "bristol", "cambridge"]
india = ["mumbai","delhi", "banglore"]
#1
city=input("enter the name of city: ")
if city in india:
    print('INDIA')
elif city in uk:
    print('UK')
elif city in usa:
    print('USA')
else:
    print("don't know")
#2
city1=input("enter the city 1  " )
city2=input("enter the city 2  ")

if city1 and city2 in india:
    print('INDIA')
elif city1 and city2 in uk:
    print('UK')
elif city1 and city2 in usa:
    print('USA')
else:
    print("don't know")

#For-while loop
    
"""1. After flipping a coin 10 times you got this result,
    result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
    Using for loop figure out count for “heads”

2. Your monthly expense list (from Jan to May) looks like this,
   expense_list = [2340, 2500, 2100, 3100, 2980]
   Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. If expense is not found then convey   that as well

3. Write a program that prints following shape, (Hint: Use for loop inside another for loop)

    *

    **

    ***    

    ****

    *****  """
#1
    
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count=0
heads=0
for item in result:
    if item=="heads":
        count=count+1
print("Head counts:",count)

#2

month_list = ["January", "February", "March", "April", "May"]
exp = [2340, 2500, 2100, 3100, 2980]
amt=input("Yur expense amount: ")
amt=int(amt)
i=0
month=-1
for i in range(len(exp)):
    if amt==exp[i]:
        month=i
        break
if month != -1:
    print('You spent',amt,'in',month_list[month])
else:
    print('You didn\'t spend',amt,'in any month')
#3
    
for i in range(1,6):
    s = ''
for j in range(i):
    s += '*'
    print(s)
 
#Functions
""" 1. Write a function called calculate_area that takes base and height as an input arguments and returns an area of a triangle as an output. Here is the equation for an area of a triangle,
       Triangle Area = ½*base*height

2. Modify above function to take third parameter called shape type. Shape type could be either triangle or rectangle. Based on shape type it should calculate area. Equation for rectangle’s area is,
   Rectangle Area = length*width
   If no shape is supplied then assume it to be triangle.
   
3. Write a function called print_pattern that takes integer number as argument and prints following pattern if input number is 3,

    *
    **
    ***

If input is 4 then it should print,
    *
    **
    ***
    ****
 Also if user doesn’t supply any argument then it should assume input to be 5."""

#1
def calculate_area(base,height):
    area=1/2*base*height
    print("Area of triangles is ",area)
    return area
base=input("enter base ")
height=input("enter height")
base=int(base)
height=int(height)
area=calculate_area(base,height)

#2
def calculate_area(a,b):
    if shape_type=="rectangle":
        area=a*b
        print("Area of rectangle is ",area)
    elif shape_type=="triangle":
        area=1/2*a*b
        print("Area of triangles is ",area)
    else:
        print("shape entered is not defined")
    return area
base=input("enter base ")
height=input("enter height ")
base=int(base)
height=int(height)
shape_type=input("Enter the shape type ")
area=calculate_area(base,height)

#3
def print_pattern(n=5):
    for i in range(n):
        s=''
        for j in range(i+1):
            s=s+'*'
        print(s)
    return s
n=input("Enter no. ")

#DICTIONARIES AND TUPLES
"""Exercise
1. Write python program that allows to store age of your family members.
   Program should ask to enter person name and age and once you are done you should be able to input name of the person 
   and program should tell the age. Now print name of all your family members along with their ages.

2. Write a function called add_and_multiply that takes two numbers as input and it should return sum and multiplication as 
   two separate numbers."""
def age_dictionary():
    d={}
    for i in range(1,4):             #apni marzi se kiya hai
        name=input("enter the persons name: ")
        age=input("enter his/her age: ")
        d[name]=age
    print("Enter the name of person whose age is required :")
    name=input()
    if name in d:
        print("age of",name,"is",d[name])
    else:
        print("I don't know the age of",name)
    print ("Age dictionary program is finished now")
age_dictionary()

#2
def add_and_multiply(a,b):
    sum=a+b
    multiply=a*b
    return sum ,multiply
a=2
b=3
s,m=add_and_multiply(a,b)
print("sum:",s,"multiplication:",m)


import calendar
cal=calendar.month(2020,9)

calendar.isleap(2019)
dir(calendar)

#READING/WRITING FILES
"""File input.txt contains numbers separated by comma as shown below,

6,8

7,6

2,8

9,5

9,6

(a) Write a function countNum(file_name,num) such that it returns number of occurrences of a number in that file. for example,

countNum(“input.txt”,9) should return 2

countNum(“input.txt”,100) should return 0

(b) Change input.txt so that when program ends it contains sum of all numbers in a line as shown below,

6,8,sum: 14

7,6,sum: 13

2,8,sum: 10

9,5,sum: 14

9,6,sum: 15  """

#basic operations
""""r"   Opens a file for reading only.
"r+"  Opens a file for both reading and writing.
"rb"  Opens a file for reading only in binary format.
"rb+" Opens a file for both reading and writing in binary format.
"w"   Opens a file for writing only.
"a"   Open for writing.  The file is created if it does not exist.
"a+"  Open for reading and writing.  The file is created if it does not exist."""

#try
f=open("E:\\machine learning\\file.txt","r")
f_out=open("E:\\machine learning\\file_wc.txt","w")
#f.write("i love c++")
for line in f:
    tokens=line.split(' ')
    f_out.write(line+' Wordcount : '+str(len(tokens)))
    print(str(tokens))    
#print(f.read())
f.close()
f_out.close()

#1
file_path=open("E:\\machine learning\\input.txt","w")
file_path.write("6,8,7,6,2,8,9,5,9,6")
file_path.close()
def countNum(file_path,num):
    count=0
    f=open(file_path,"r")
    for line in f:
        tokens=line.split(',')
        for token in tokens:
            if num==int(token):
                count=count+1
    print(count)
    return count
c = countNum("E:\\machine learning\\input.txt",3)
print("count: ",c)
#or
"""def countNum(file_path, num):
    count = 0
    with open(file_path,"r") as f:
        for line in f.readlines():
            tokens = line.split(",")
            count += count_num_in_tokens(tokens, num)
    return count
def count_num_in_tokens(tokens, num):
    count = 0
    for token in tokens:
        if num == int(token):
            count+=1
            return count """
        
#2                                                    yeh vala nhi  hua
f=open("E:\\machine learning\\input.txt","r")
#print(f.read())
f_out=open("E:\\machine learning\\input.txt","a")
def sum_numbers(file_path):
    output_lines=[]
    for line in f:
        tokens=line.split(',')
        count=0
        for token in tokens:
            count+=int(token)
        output_lines.append(line +" Sum : "+ int(count))
        f_out=f.write(output_lines)
        f_out.close()
        f.close()
sum_numbers("E:\\machine learning\\input.txt")  

#or

def sum_numbers(file_path):
    output_lines = []
    with open(file_path,"r") as f:
        for line in f.readlines():
            tokens = line.split(",")
            total = sum_tokens(tokens)
            output_lines.append("sum: " + str(total) + " | " + line)
            with open(file_path,"w") as f:
                f.writelines(output_lines)
def sum_tokens(tokens):
    sum = 0
    for token in tokens:
        sum += int(token)
        return sum
sum_numbers("E:\\machine learning\\input.txt")

if __name__=="__main__":
    print("nice")

#exception handling
x=input("enter no. : ")
y=input("enter no. : ")
try:
    z=x/int(y)
except ZeroDivisionError as e:
    print('Division by zero is exception')
    z=None
except Exception as e:
    print( "exception type:",type(e). __name__)
    z=None
print("Division is",z)

#The task of constructors is to initialize the data members of the class when an object of class is created.
#The __init__() method is called the constructor in Python and is always called when an object is created
#By using the self keyword, one can easily access all the instances defined within a class, including its methods and attributes.
#making a class

class Human:
    def __init__(self,n,o):
        self.name=n
        self.occupation=o
    def work(self):
        if self.occupation=="Engineer":
            print("ahh damm Intelligent guy")
        elif self.occupation=="doctor":
            print("great memory")
        else :
            print("Aap sharma ji ke ladke nhi ho ")
    def speaks(self):
        print(self.name,"is a ",self.occupation)
daksh=Human("Daksh","Engineer")
daksh.work()
daksh.speaks() 

rishabh=Human("Rishabh","doctor")
rishabh.work()
rishabh.speaks()

yash=Human("Yash","andha paisa")
yash.work()
yash.speaks           

#iterator
for i in range(8):
    print(i)
a=['hey','my','name','is','daksh']
itr=iter(a)
next(itr)

a=['hey','my','name','is','daksh']
itr=reversed(a)
next(itr)
#for example
class RemoteControl():
    def __init__(self):
        self.channels=['HBO','Hotstar','Netflix','Prime']
        self.index=-1
    def __iter__(self):
        return self
    def __next__(self):
        self.index +=1
        if self.index==len(self.channels):
            raise StopIteration
        return self.channels[self.index]
r=RemoteControl()
itr=iter(r)
next(itr)


        

  

            
    
        




        
    







