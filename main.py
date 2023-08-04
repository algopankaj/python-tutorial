

# ******************************************* Chapter one *********************************************************

# Guido van Rossum. ()

# print("hello world ") # print is use to print something on screen.

# String --> collections of characters inside "double quotes" or 'single quotes'  

# print('Hello world')   
# print('hello "pankaj" pankaj')
# print("I'm pankaj")

#  print(i, end=" ")   # This will print in only and only one line with space.

# Ecacpe squences 

# print("hello \"pankaj\" chauhan") 

# print("Line A \nLine B")   # \n is use for new line

# output : This is \\ Double Backslash 
# print(r"This is \\ Double Backslash")

# output : This is /\/\/\/\/\ Mountains  
# print(r"This is /\/\/\/\/\ Mountains")  # r is used to print what ever you have written within quotes (raw string) 

# output : He is    Awesome
# print(r"He is \tAwesome")

# # output : \" \n \t \'
# print(r" \" \n \t \'")

# python as a calculator .............
# print(2+2)
# print(2+5*9)
# print(10/2) # / floating point division
# print(10//2) # Integer division
# print(2**3) # Exponent 2 ki power 2
# print(9**0.5) # square root of 9
# print(2**0.5) # Square root of 2 , it is giving 1.4142135623730951 as output so we will round this value upto 4 digits by rounf method
# print(round(2**0.5,4)) # It will round the square root value
# print(3%2) # modulo gives us reminder
# print((2+3)*6/2)  # Highest prec is () then & and / , left to right
# print(2**3**2) # precedence rule, will evaluate right to left

# Precedence Rule ............  # Visit : https://docs.mql4.com/basis/operations/rules
# Operators                              Precedence and associativity rule.
# Parenthese                                    Highest
# Exponent                                      Right to Left
# *,/,//,%                                      Left to Right
# +,-                                           Left to Right 

# Variables in python................
# number1=3
# print(number1)
# first_name="Pankaj"
# second_name="Chauhan"
# full_name=first_name+" "+second_name 
# print(full_name)

# Variables naming convention ..
# Always try to write into snake  case like ( user_name , first_name )
# You can't start with (numbers--> 1number=5 , $name='pankaj) You can't use special char ($,&) into your variable.


# ************************************ summary of chapter one ************************************************:
# print function
# escape sequence
# escape sequence as normal text
# python as calculator
# variables
# naming rules for variables
# convention for variable naming


# ******************************************* Chapter Two (Strings) *********************************************************

# Strings 
# Collections of characters inside double quote or single quotes ..

# first_name='Pankaj'
# second_name='Chauhan'
# full_name=first_name+" "+second_name
# print(full_name+3)  # error
# print(full_name + str(4)) no error

# input function........................

# name =input("Type your name")
# print(name)
# print("Hello " + name)


# one=int(input("enter first number")) # Without using casting operator it will take input into string. 
# two=int(input("Enter second number"))
# print(one+two)
# total_sum= one+two
# print("Your sum is" + str(total_sum)) # str --> change int to string.
  
# str
# 45----->"45"

# int
# "45"-----> 45

# float
# 4--->4.0

# first=int("5")
# second=int("dc")
# print(first+second)

# x=y=z=1   # Assign value to multi variable.. 
# print(x+y+z)
 
# name ,age="pankaj","34"
# print("Hi"+name+ "welcome")

# name ,age=input("enter your name and age").split()
# print("your name is"+name+"and your age is"+age )  # ugly syntax.


# a, b=input().split(",")

# a=int(a)
# b=int(b)
# print(a+b)


# name,age=input("Enter your name and age ").split(",")
# python--> 3.6 syntax
# print(f"you'r {name} and your age is {age}")

# Exercise 1........

# a,b,c=input("Enter three number using common").split(",")
# a=int(a)
# b=int(b)
# c=int(c)
# d=(a+b+c)/3
# print(f"Average of three number is {(int(a)+int(b)+int(c))/3}")  or
# print(f"Average of this three number is {d}")

#  String indexing............

# language="python"

#  position(index)
#  p =  0  -6
#  y =  1  -5
#  t =  2  -4
#  h =  3  -3
#  o =  4  -2
#  n =  5  -1

# String slicing / string substring.

# Syntax - [start_index : end_index(ecluded) ]

# lang='python'
# print(lang[-3:6])     # hon
# print(lang[1:])       # ython
# print(lang[:3])       # pyt
# print("Pankaj"[2:5])  # nka

# Step argument.............  

# print("Pankaj"[1:4:2])  # ak

# language="Khalastani"
# print(language[::-1])   # This is used to reverse the string .

# name=input("Input your name")
# print(name[::-1])

# String functions ....................

# name ="PanKaJ cHauHaN"

# print(len(name))         # Calculate the len of string    
# print(name.lower())      # Convert into small alphabets 
# print(name.upper())      # Convert into capital alphabets
# print(name.title())      # Convert into title 
# print(name.count('a'))   # Count the particular character into string.



# Exercise ......................

# Take two comma separated inputs from user
# 1.) user's name example="Harshit"
# 2.) a single character ='h'

# output - 2 print lines
# 1.) user's name length
# 2.) count the character that user inputed (bonus : case insensitive count )


# Solution .....................

# user_name,a_char=input("Enter you name and that character ! ").split(",")

# print(len(user_name))                  # Printing the length of the user_name
# user_name=user_name.lower()            # Converting to the lower_case
# a_char=a_char.lower()                  # Converting to the lower case
# print(user_name.count(a_char))         # counting the no of a_char present into the user_name


# Strip method ..................

# name = "     Harshit    "
# dots="...................."

# print (name + dots)                    # Add two string..
# print(name.lstrip() + dots)            # Remove the left speaces.
# print (name.rstrip() + dots)           # Remove the right sapces.
# print(name.strip() + dots)             # Remove the complete spaces.
# print(name.replace(" ","") + dots)     # This method will also work as strip method


# find() , replace() method ..................

# string="she is beautiful and she is good dancer"
# print(string.replace(" ","_"))
# print(string.replace("is","was"))
# print(string.replace("is","was",1))

# print(string.find("is"))
# print(string.find("is",6)) 


# Center method .............................

# name = "harshit"
#4 “tharshiter , 11
# print(name.center(11,"*"))
# name = input("enter your name : ")
# print (name. center (len(name)+8, "*"))


# Strings are immutable in python why ? ......................

# strings are immutable

# string = "string"
# string[1]='r' # you can't do this you will get an error.
# new_string = string.replace('t', 'T')
# print(new_string)
# print(string)


# Assignment operator ...........................

# name ="Harsh"
# name+="it"
# print(name)


# ***************************************Summary of chapter two*****************************************************

# strings
# string indexing
# string slicing
# take user input
# take two user inputs
# len function
# lower, upper, title method
# find, replace, center method
# strings are immutable




# ************************************* Chapter Three (Conditional Statement & loops) *******************************

# syntax
# if condition:
#     # code            # If condition is true then this code will execute
#     # code

# age=input("Enter your age")
# age=int(age)

# if age>=14:
#     print("You are above 14")
#     print("This is for the if condition !")


# if_else condition.....

# age=12

# if age>=14:
#     print("You are above 14")
#     print("This is for the if condition !")
# else:
#     print("No you can't play !")

# pass statement ...( when you don't want to do anything )

# if age>56:
#     pass

# Exercise.......

# EXERCISE , NUMBER GUESSING GAME
# Make a variable, like winning_number and assign any number to it.
# Ask user to guess a number .
# if user guessed correctly then print "YOU WIN !!!1"
# if user didn't guessed correctly then :
# if user guessed lower than actual number then print “too low"
# if user guessed higher than actual number then print "too high"
# google "how to generate random number in python " to generate random
# winning number


# Program to generate a random number between 0 and 9
# importing the random module


# import random
# winning_number=random.randint(0,9)

# guess_number=int(input("Guess any number !"))

# if winning_number==guess_number:
#     print("YOU WIN")
# else:
#     if winning_number>guess_number:
#         print("TOO LOW")
#     else:
#         print("TOO HIGH")


# And ,or operator.........
# check two conditions at same time
# and , or

# name = "abc"
# age = 19

# if name=="abc" and  age==19:
#     print(" condition True")
# else:
#     print("condition False")


# Or condition

# if name=="abc" or  age==19:
#     print(" condition True")
# else:
#     print("condition False")


# EXERCISE - WATCH COCO

# Ask user's name and age
# If user's name start with ('a’ or 'A') and age is above 10 then
# Print "you can watch coco movie’
# Else print ‘sorry, you cannot watch coco’

# name,age=input("Enter your name and age using space").split(" ")
# age=int(age)
# start_name=name[0]

# if (start_name=='a' or start_name=='A') and age>=10:
#     print("you can watch coco movie")
# else:
#     print("Sorry you can't watch !")



# if elif else statement
# show ticket pricing

# 0 to 3 (free)
# 4 to 10 (150)
# 11 to 60 (250)
# above 60 (200)

# age=int(input("Enter your age !"))

# if 1<=age<=3:
#     print("Ticket Price is Free !!")
# elif 4<=age<=10:
#     print("Ticket Price is 150 !!")
# elif 11<=age<=60:
#     print("Ticket Price is 250 !!")
# else:
#     print("Ticket price is 300 !!")


# in keyword with if.  (It is used to check that a particular char is present in string or not )
# name="vivek"

# if 'a' in name:
#     print("A is present in name !")
# else:
#     print("A is not present in name")


# check empty or not ..................

# name="Pankaj"

# if name:
#     print(f"You typed {name}")
# else:
#     print("ypu did't type anything ")


#loops......
# while loops ,for loops

# i=1
# while i<=10:
#     print(f"Print Hello World !{i}")
#     i=i+1

# sum of number using while loop : (1 to 10 )

# sum=0
# i=1
# while i<10:
#     sum+=i
#     i+=1
# print(sum)


# exercise one of three

# sum of n natural numbers
# ask a user for natural number (n)
# print total from 1 to n n


# sum=0
# n=int(input("Input the number !"))
# i=1
# while i<=n:
#     sum+=i
#     i+=1
# print(sum)



# problem

# ask user to input a number containing more than one digit
# example - 1256
# calculate 1+2+5+6 and print
# algorithm - (method to solve problem in human language)
# ask input in string, i.e don't change string to int


# example - "1256"
# pick string character one by one and change to int
# int(example[0]) + int(example[1]) .... go upto len(example)

# 1...........

# number=input("Enter a number")
# sum=0
# len=len(number)
# i=0

# while i<len:
#     num=int(number[i])
#     sum+=num
#     i+=1
# print(sum)


# ask a user for name
# Example - Harshit Vashisth
# print count of each words
# output :

        #H:1

        #a:2

        #r:1

        #s:3

        #h:3

        #i:2

        #t:2

        # :1

        #V:1

# string="Harshit Vashishth"
# temp_var=""
# i=0

# while i<len(string):
#         if string[i] not in temp_var:
#                 temp_var+=string[i]
#                 print(f"{string[i]} : {string.count(string[i])}")
#         i+=1


# infinite loop ....
# i=0
# while i<=10:
#     print(f"Hello world {i}")


#for loop

# for i in range(1,10):
#     print(f"Hello world {i}")


# sum from 1 to 10 ....
# 1+2+3+4..........+10

# sum=0
# for i in range(1,11):
#     sum+=i
# print(sum)

# Exercise ......

# n=int(input("Enter the number !"))
# total=0
# for i in range(1,n):
#      total+=i
# print(total)

# Practice for loop
# Ask user a number 1256
# Calculate sum of digits 1+2+5+6

# number=input("Enter the number !")
# sum=0

# for i in range(0,len(number)):
#     sum+=int(number[i])
# print(sum)


# ask a user for name
# Example - Harshit Vashisth
# print count of each words
# output :

        #H:1

        #a:2

        #r:1

        #s:3

        #h:3

        #i:2

        #t:2

        # :1

        #V:1

# solve using for loop...
# string ="Harshit Vashishtha"

# len=len(string)
# temp_val=""
# for i in range(0,len):
#     if string[i] not in temp_val:
#         temp_val+=string[i]
#         print(f"{string[i]} : {string.count(string[i])}")


# Break and Continue Keywords................

# 1 to 10 print....

# for i in range(1,10):
#     if i==5:
#         break
#     print(i)

# 1 to 10 print.....

# for i in range(1,10):
#     if i==5:
#         continue
#     print(i)

# Modify the  number gusseing game...

# winning_number = 43
# guess = 1
# number = int(input("guess a number between 1 and 160 : "))
# game_over = False

# while not game_over:
#         if number == winning_number:
#                 print(f"you win, and you guessed this number in {guess} times ")
#                 game_over = True
#         else:
#                 if number < winning_number:
#                         print("too low ")
#                         guess += 1
#                         number = int(input("guess again : "))
#                 else:
#                         print("Too High")
#                         guess+=1
#                         number=int(input("guess again !"))


# Step argument in range function .....

# for i in range(1,10 ,2): # Here 2 is working as a step argument to increase number ..
#         print(i)

# for i in range(10 ,0,-2):
#     print(i)

# for using in string.........

# name="Harshit"
# for i in name:
#     print(i)


# 1256---->1+2+5+6

# num=input("Enter the number !")
# total=0
# for i in num:
#     total+=int(i)
# print(total)



#  ..................................... Chapter 4 Functions ........................................................


# functions...
# name="pankaj"
# print(len(name)) # len --> function.

# # Add two numbers 
# def add_two(a ,b):
#     return a+b

# sum=add_two(5,4)
# print(sum)
 

# Exercise . Take 2 number input form user and print the output using the function...

# def add_two(num1,num2):
#     return num1+num2

# a=int(input("Enter first number : "))
# b=int(input("Enter second number : "))

# sum=add_two(a,b)
# print(sum)


# print vs return in python....

# def add_three(a,b,c):
#     print(a+b+c)

# add_three(5,6,7)


# def add_three(a,b,c):
#     return a+b+c

# sum=add_three(5,6,7)
# print(sum)

# Function practice ..
# task 1 . take a name as argument in function and return the last character of the name.

# def find_last(name):
#     return name[-1]

# ans=find_last("pankaj")
# print(ans)

# task 2 . check the given number is odd or even ....

# def check(num):
#     if num%2==0:
#         return "even"
#     else:
#         return "odd"
    
# num=int(input("Enter any number to check odd or even !"))
# guess_odd_even=check(num)
# print(guess_odd_even)

# Exercise 
# task 1. take 2 number input form the user and check the which number is bigger...

# def check(a,b):
#     if a>b:
#         return "a is greater then b"
#     return "b is greater then a"

# a=int(input("Enter first number ! "))
# b=int(input("Enter second number ! "))

# ans=check(a,b)
# print(ans)

# task 2. check greatest among 3 numbers.

# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     else:
#         if b>a and b>c:
#             return b
#         return c

# a=int(input("Enter first number ! "))
# b=int(input("Enter second number ! "))
# c=int(input("Enter third number ! "))

# ans=greatest(a,b,c)
# print(ans)



# Exercise .........
# Define is_palindrome function that take one word in string as input
# and return True if it is palindrome else return False

# palindrome - word that reads same backwards as forwards


# example
# is_palindrome("madam”) ------> True
# is_palindrome(“naman”) ------> True
# is_palindrome("horse”™) ------> False
# logic (algorithm)

# 1st Method 
# def is_palindrome(string):
#     length=len(string)
#     for i in range(0,length):
#         if string[i] != string[length-i-1]:
#             return False
#     return True

# ans=is_palindrome("Pankaj")
# print(ans)


# 2nd Method ...

# def is_palindrome(string):
#     if string==string[::-1]:
#         return True
#     return False

# ans=is_palindrome("Pankaj")
# print(ans)    


# Fibonacci series .....
# 0 1 1 2 3 5 8 13 21 34 .......

# def fibonacci_seq(n):             ( This is not working i dont know why i need to know ! )
#     if n<=1:
#         return n
#     first=fibonacci_seq(n-1)
#     second=fibonacci_seq(n-2)
#     return first+second

# n=int(input("Enter the number ! "))
# ans=fibonacci_seq(n)
# print(n)


# def fibonacci_seq(n):
#     a=0
#     b=1
#     if n==1:
#         print(a)
#     elif n==2:
#         print(a, b)
#     else:
#         print(a, b,end=" ")
#         for i in range(n-2):
#             c=a+b
#             a=b
#             b=c
#             print(c, end=" ")
   
# fibonacci_seq(200)

# Default parameters............

# def user(first_name,second_name,age=23):
#     print(f"Your first name is {first_name}")
#     print(f"Your second name is {second_name}")
#     print(f"Your age is {age}")


# print(user('pankaj','kumar'))

# Scope variable......

# def func():
#     x=7
#     return x

# def func2():
#     return x  // You can't print the variable which is out of scope.



#  ............................................   Chapter 5 List  ....................................................

# data structures
# List ---> this chapter
# ordered collection of items
# you can store anything in lists int, float, string

# numbers=[1,2,3,4]
# print(numbers)
# print(numbers[1])

# words=['word1','word2','word3']
# print(words)
# print(words[1])

# mixed=[1,2,4,'word1','word2',2.3,None]
# print(mixed)
# print(mixed[0])

# how to add items to our List
# most common thing that you can do with your List and most important

# fruits=['grapes','apple']
# fruits.append('mango')     # It will add data at the last.
# print(fruits)


# fruits=[]
# fruits.append('mango')
# fruits.append('grapes')
# print(fruits)


# some more methods to add data in our List
# insert method 
# how to join(concatenate) two List
# extend method
# difference between append and extend method

# fruits1=['grapes','mango']
# fruits1.insert(1,'guava')      # It is used to add element at specific position...
# print(fruits1)
# fruits2=['apple','orange']

# fruits=fruits1+fruits2         # Simply adding two list..
# print(fruits)

# fruits1.append(fruits2)
# fruits1.extend(fruits2)        # This will simply add list into another list (List inside list)
# print(fruits1)
# print(fruits2)

# common methods to delete data from List
# fruits = ['orange', 'apple', 'peer', 'banana', 'kiwi']
# pop method
# fruits.pop()                   # This will delete last element (Default)
# fruits.pop(1)
# del fruits[1]
# fruits.remove('banana')        # This will delete particular element .
# print(fruits)
# append ,inssert ,extend        # Use to add element.
# pop ,remove, del               # Use to delete element.

# in keywords with list:

# fruits = ['orange', 'apple', 'peer', 'banana', 'kiwi']

# if 'apple' in fruits:
#     print("Apple is present into the list")
# else:
#     print("Not present into the list !")


# count
# sort method
# sorted function
# reverse
# clear
# copy


# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

# cnt=fruits.count('apple')
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# fruits3=fruits.copy()
# print(fruits3)

# Compare list
# is vs equal.... (==, is) 


# fruits1= ['orange', 'apple', 'pear']
# fruits2= ['orange', 'apple', 'pear']
# fruits3= ['banana', 'kiwi', 'apple', 'banana']

# print(fruits2==fruits3)               # It checks that value of list are same or not .
# print(fruits1 is fruits2)             # It checks that is it stored at same memory location...


# split method
# convert string to List

# user_info="Pankaj,24".split(',')
# print(user_info)                   # ['Pankaj', '24']

# join method
# convert List to string

# user_info=['pankaj','24'] # both will be string.
# print(','.join(user_info))


# list vs strings

# strings are immutable

# s='pankaj'
# t=s.title()
# print(t)
# print(s)



# Lists are mutable
  
# list=[4,5,6,7,8,9]
# list[0]=67
# print(list)
# list.pop()
# print(list)


# Looping into list ...

# fruits=['orange','apple','pear','banana','kiwi']

# for fruit in fruits:
#     print(fruit,end=' ')

# i=0

# while i<len(fruits):
#     print(fruits[i])
#     i+=1



# List inside list....

# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# print(matrix[0])
# print(matrix[0][0])

# for sublist in matrix:
#     for i in sublist:
#         print(i)

# s="string"
# print(type(s))


# generate Lists with range functions
# numbers=list(range(1,11))
# something more about pop method
# poped_item=numbers.pop()
# print(poped_item)

# index method
# print(numbers.index(1))

# pass List to a function

# def negative_list(l):
#     list=[]
#     for i in l:
#         if i<0:
#             list.append(i)
#     return list

# l=[-2,4,7,-7,-5]
# list_s=negative_list(l)
# print(list_s)

# Exercise 1.

# define a function which will take list containing numbers as input
# and return list containing square of every elements

# example
# numbers = [1,2,3,4]
# square_list(numbers) ----> return ----> {1,2,9,16]


# def square(l):
#     ans=[]
#     for num in l:
#         ans.append(num*num)
#     return ans

# l=[1,2,3,4]
# ans=square(l)
# print(ans)


# Exercise 2..

# define a function which will take list as a argument and this function
# will return a reversed list

# examples
#[1,2,3,4] --- > [4,3,2,1]
# ['wordl', 'word2'] ---> ['word2', 'word1']

# Note you simply do this with reverse method or [3:1]

# but try to do this with the help of append and return method

# Solution 1..
# Method 1.
# def first_sol(l):
#     ans=[]
#     ans=l[::-1]
#     return ans

# list=[1,2,3,4,5]
# ans=first_sol(list)
# print(ans)

# Method 2

# def second_sol(l):
#     ans=[]
#     for i in range(0,len(l)):
#         ans.append(l.pop())
#     return ans

# list=[1,2,3,4,5]
# ans=second_sol(list)
# print(ans)

# Exercise 2.

# define a function that take list of words as argument and
# return list with reverse of every element in that list

# example
# [‘abc’, 'tuv', 'xyz'] ---> ['cba’, ‘wut’, 'zyx']

# def reversed(l):
#     ans=[]
#     for word in l:
#         rev_word=word[::-1]
#         ans.append(rev_word)
#     return ans

# list=['abc','tuv','xyz']
# ans=reversed(list)
# print(ans)

# Exercise 3.

# filter odd even
# define a function
# input
# list ---> [1,2,3,4,5,6,7]
# ouput ----> [[1,3,5,7], [2,4,6]]

# def filteration(l):
#     ans=[]
#     odd=[]
#     even=[]
#     for i in range(0,len(l)):
#         if l[i]%2==0:
#             even.append(l[i]) 
#         else:
#             odd.append(l[i])
#     ans.append(odd)
#     ans.append(even)
#     return ans

# list=[1,2,3,4,5,6,7]
# ans=filteration(list)
# print(ans)


# Exercise 4.

# common elements finder function
# define a functions which take 2 lists as input and return a list
# which contains common elements of both lists

# example
# input ---> [1,2,5,8], [1,2,7,6]
# output ---> [1,2]


# def common(l1,l2):
#     ans=[]
#     for i in l1:
#         if i in l2:
#             ans.append(i)
#     return ans       

# l1=[1,2,5,8]
# l2=[1,2,7,6]
# ans=common(l1,l2)
# print(ans)


# min and max function....

# numbers=[6,20,2]

# print(min(numbers))      # Min number from the list.
# print(max(numbers))      # Max number from the list.

# def greatest_diff(l):
#     return max(l)-min(l)

# l=[2,60,4]
# print(greatest_diff(l))

# Exercise 5.

# last exercise
# function
# [1,2,3, [1,2], [3,4]] , input
# Output :2
# Hint : type()

# def sublist_counter(l):
#         count = 0
#         for i in l:
#              if type(i) == list:
#                 count += 1 
#         return count        


# mixed = [1,2,3, [1,2], [3,4]]
# print(sublist_counter(mixed))


#..................................................Summary of chapter 5 ............................................

# list chapter summary

# list is a data structre that can hold any type of data
# create a list

# words= ['word1', 'word2']

# you can store anything inside list
# mixed = [1,2,3,[4,5,6],'seven',8.0, None]

# list is ordered collection of items
# print(mixed[0])                                 # ouput = 1
# print(mixed[3])                                 # output = [4,5,6]

# add data to our list
# append method

# mixed.append('10')
# print(mixed)
# mixed.append([10,20,30])
# print(mixed)



# ............................................. Chapter 6 Tuples ..................................................


# tuple data structure
# tuple can store any data type 
# most important tuples are immutable, once tuple is created you can't update
# data inside tuple

# example = ('one', 'two', 'three')
# no append , no insert , no pop , no remove  
# days = (‘monday’, 'tuesday')
# tuples are faster than lists
# methods
# count, index
# len function
# slicing
#example[0] = 1  Try to do this you will get error..


# looping in tuples
# tuple with one element
# tuple without parenthesis
# tuple unpacking
# list inside tuple
# some functions that you can use with tuples

# mixed=(1,2,3,4.0)
# print(type(mixed))

# for i in mixed:
#     print(i)
# Note you can use while loop too.


# Tuple with one element..

# nums=(1,)
# print(nums)
# print(type(nums))


# Tuple without parathensis....

# fruits='banana','kiwi','apple'
# print(type(fruits))

# Tuple unpacking ....

# fruit1,fruit2,fruit3=(fruits)
# print(fruit1)
# print(fruit2)
# print(fruit3)


# List inside tuple .....

# favourite=('maneli jamal',['rawat','andrew foy'])
# print(favourite)

# min , max , sum

# tuple=(1,4,6,7,8,9)
# print(min(tuple))
# print(max(tuple))


# Function returning two values......

# def func(num1,num2):
#     add=num1+num2
#     mult=num1*num2
#     return (add ,mult)

# print(func(2,4))
# add,mult=func(2,4)
# print(add,mult)


# Something more about tuple ,list ,str.

# nums=tuple(range(1,11))
# nums=list(range(1,11))
# nums=str(tuple(range(1,11)))
# print(nums)



#............................................... Summary of chapter 6 ..............................................

# tuples
# tuples are immutable
# tuples are ordered collections of data
# tuples can store any data type
# you cannot change(add or delete) values from tuple once it created
# but can add, delete data from list which is present inside tuples

# mixed = (1,2,3,4,5,"six")

# no append , no pop , no insert , no remove
# only count and index

# functions
# min(), max(), len(), sum()

# mixed2 = (1,2,3,4,5,[6,7,8])
# mixed2[5].pop()
# print(mixed2)


# .......................................... Chapter 7 Dictionaries ................................................


# dictionaries intro

# Q- why we use dictionaries?  
# A - Because of limitations of lists , lists are not enough to represent
# real data .

# Example
# user = ['Harshit', 24, ['coco', 'kimi no na wa'], ['awakening', 'fairy tale']]
# this list contains user name , age , fav movies , fav tunes
# you can do this but this is not a good way to do this.


# Q - what are dictionaries
# A - unordered collections of data in key : value pair.

# How to create dictionaries ......

# user={'name':'Harshit','age':24}
# print(user['name'])
# print(user)
# print(type(user))

# Second way to create dictionaries....

# user1=dict(name='Pankaj',age=46)
# print(user1)
# print(type(user1))

# user_info={
#     'name':'Pankaj',
#     'age':23,
#     'fav_movies':['joe','ditres','flaw','distro']
# }

# print(user_info)
# print(type(user_info))
# How to excess data into dict.
# print(user_info['fav_movies'])

# How to add data to empty dictionaries......

# user_info2={}
# user_info2['name']='Pankaj'
# user_info2['age']=12
# print(user_info2)


# in keyword and iterations in dictionary

# user_info = {
#         'name' : 'Pankaj',
#         'age': 24,
#         'fav_movies' : ['coco’, ‘kimi no na wa'],
#         'fav_tones' : ['awakening', 'fairy tales']
# }
# print(user_info)
# print(type(user_info))

# check if key exist in dictionary
# if 'name' in user_info:
#     print('present')
# else:
#     print('not present')

# check if value exist in dictionary

# if 'Pankaj' in user_info.values():
#     print('present')
# else:
#     print('not present')

# loops in dictionaries

# Print the keys.
# for i in user_info:            # It will print all the keys 
#     print(i)

# Print values
# for i in user_info.values():   # It will print all the values
#     print(i)


# values method
# user_info_values = user_info.values()
# print (user_info_values)
# print(type(user_info_values))

# Keys method
# user_info_keys = user_info.keys()
# print (user_info_keys)
# print(type(user_info_keys)) |


# Item method ..

# user_items=user_info.items()
# print(user_items)
# print(type(user_items))
# [('name', 'Pankaj'), ('age', 24), ('fav_movies', ['coco’, ‘kimi no na wa']), ('fav_tones', ['awakening', 'fairy tales'])]


# add and delete data
# user_info = {
#         'name' : 'Pankaj',
#         'age': 24,
#         'fav_movies' : ['coco’, ‘kimi no na wa'],
#         'fav_tones' : ['awakening', 'fairy tales']
# }
# how to add data.
# user_info['fav_songs']=['rabta','sanam teri kasam','ham mar jayenge']
# print(user_info)


# pop method.
# poped_item=user_info.pop('fav_tones')
# print(f"Popped item is{poped_item}")
# print(user_info)

# popItem method.

# popped_item=user_info.popitem()
# print(user_info)
# print(popped_item)

# fromkeys ( Its used to create dictionary)
# d={'name':'unknown','age':'unknown'}

# d=dict.fromkeys(['name','age','fav_mov'],'unknown')
# print(d)

# d=dict.fromkeys(range(1,5),'unknown')
# print(d)

# get method(useful)
# d={'name':'Pankaj','age':'unknown'}
# print(d.get('name'))

# d.clear()  Used to clear the dictionary .
# print(d)

# d1=d.copy()  Used to 
# print(d1)


# exercise
# define a function that takes a number(n)
# return a dictionary containing cube of numbers from 1 to n

# example
# cube_finder(3)
# {1:1, 2:8, 3:27}

# def cube_finder(tup):
#     ans={}
#     for i in tup:
#         ans[i]=i**3
#     return ans


# tup=tuple(range(1,11))
# ans=cube_finder(tup)
# print(ans)

# write a program for word counter ....

# def word_counter(s):
#     ans={}
#     for i in s:
#         ans[i]=s.count(i)
#     return ans

# string ="pankaj"
# ans=word_counter(string)
# print(ans)


# take the input from the users Like below ...
# users = {
# 'name' : 'Harshit',
# 'age' : 24,
# 'fav_movies' : ['coco', 'avangers'],
# 'fav_songs' : ['songl', 'song2']
# }

# user={}
# name=input("What is your name : ")
# age=int(input("What is your age : "))
# fav_movies=input("Enter your favourite movies seperated by comma : ").split(",")
# fav_songs=input("Input your favourite songs sepreated by comma : ").split(",")

# user['name']=name
# user['age']=age
# user['fav_movies']=fav_movies
# user['fav_songs']=fav_songs

# print(user)



#  ......................................... Chapter 8 Set .......................................................

# unordered collection of unique items..

# s={1,2,3,4,4,2}
# print(s)

# Important  
# l=[1,2,4,45,756,4,4,4,4,3,3,3,7,9,8,2,1,3,5,6]
# set=set(l)
# l=list(set)
# print(l)

# We can have different datatypes into the set ...

# s.add(4)
# s.add(5)
# s.remove(5)  (if the element is not present into set in will give an error )
# s.discord(5)  (It won't through error if the element is not present )
# s.clear()   (clear the set)
# s.copy()    ( make the copy of set )
# print(s)

# s1={1,2,3,4}
# s2={3,4,5,6}

# Union             ( | )
# Intersection      ( &  )

# union_set=s1 | s2
# intersect_set=s1 & s2
# print(union_set)
# print(intersect_set)

# in keyword in set and for loop (in keyword is used to check if the item is present or not in set)
# s={'a','b','c'}

# if 'd' in s:
#     print("Present")
# else:
#     print("Not present")

# FOR loop 

# for item in s:
#     print(item ,end=" ")
 


# ............................................ Chapter 9 List comprehension .........................................

#  Most important 

# List comprehension
# With the help of list comprehension we can create of list in one line

# create a list of squares from 1 to 10

# ans=[]
# for i in range(1,11):
#     ans.append(i**2)

# print(ans)

# Using list comprehension ...
# squares=[i**2 for i in range(1,11)]
# print(squares)

# negative=[]
# for i in range(1,11):
#     negative.append(-i)

# print(negative)

# Using list comprehension ...
# negative=[-i for i in range(1,11)]
# print(negative)

# names=['Harshit','Mohit','Rohit']
#new_list=['H','M','R']

# new_list=[]
# for i in names:
#     new_list.append(i[0])

# print(new_list)


# Using list comprehension ...
# new_list=[name[0] for name in names]
# print(new_list)


# define a function that take list of strings
# list containing reverse of every string

# NOTE - USE LIST COMPREHENSION because we already did this exercise 
# using normal method

# example

# l=['abc', 'tu', 'xyz']
# reverse_string(1) -I--> ['bac’, ‘wut, ‘zyx']

# ans=[]
# for word in l:
#     ans.append(word[::-1])
    
# print(ans)

# ans=[word[::-1] for word in l]
# print(ans)

 
# List comprehension with if statement .........

# numbers=list(range(1,11))

# even=[]
# for i in numbers:
#     if i%2==0:
#         even.append(i)

# print(even)

# even_ans=[i for i in range(1,11) if i%2==0]
# even_ans=[i for i in numbers if i%2==0]
# print(even_ans)

# odd nums...

# odd_ans=[i for i in range(1,11) if i%2 != 0]
# print(odd_ans)


# num to string 
# define a function

# example 
# input= [True, False, [1,2,3], 1, 1.0, 3]
# output =['1', '1.0', '3']

# ans=[]
# for i in input:
#     if type(i)==int or type(i)==float:
#         ans.append(i)

# print(ans)
    
# ans=[str(i) for i in input if type(i)==int or type(i)==float]
# print(ans)


# List comprehension with if else:
# nums=[1,2,3,4,5,6,7,8,9,10]
# new_list=[-1,4,-3,8,-5,12,-7,16,-9,20]

# ans=[i*2 if (i%2==0) else -i for i in nums ]
# print(ans)

# List comprehension in nested list:

# example=[[1,2,3],[1,2,3],[1,2,3]]
# nested_comp=[[i for i in range(1,4)] for j in range(3)]
# print(nested_comp)




# ............................................. Chapter 10 Dictionaries comprehension ..............................


# squares={1:1, 2:4, 3:9}

# square={num:num**2 for num in range(1,11)}
# print(square)

# print in such manner ..
# square of 1:1
# squre of 2:4

# square={f"square of {num} is":num**2  for num in range(1,11)}
# print(square )

# for k,v in square.items():
#     print(f"squre of {k} is : " , v)

# string='Harshit'
# word_count={char:string.count(char) for char in string}
# print(word_count)

# Dictionaries comprehension with if else .
# d={1:'odd','even'}

# odd_even={i:('even' if i%2==0 else 'odd') for i in range(1,11)}
# print(odd_even)

# set comprehension---> only one video.
# s={k**2 for k in range(1,11)}
# print(s)



# Chapter 11 ( *args )........................................................................


# make flexible functions.

# (*operator) or (* args ) 

# def total(a,b):
#     return a+b


# def all_total(*args):
#     print(args)                       # tuple()
#     print(type(args))
#     print(sum(args))                  # This will print the sum of the tuple 

# all_total(1,2,3,4,5) 


# def all_total(*args):
#     total=0
#     for num in args:
#         total+=num 
#     return total

# sum=all_total(1,2,3,4,5) 
# print(sum)


# *args with normal parameters ...

# def multiply_nums(num,*args):
#     multiply=1
#     print(num)  #2
#     print(args)  # 2,3
#     for i in args:
#         multiply*=i
#     return multiply

# mult=multiply_nums(2,2,3)  # 2 will be allocated to the num variable and rest (2,3) argument will be assign to the *args
# print(mult)


# def all_total(num1,num2,*args):    # Here 1,2 will be assign to the num1 ,num2 and rest 
#     mult=1                         # of the number will assign to the args.
#     for num in args:
#         mult*=num 
#     return mult

# mult=all_total(1,2,3,4,5) 
# print(mult)
 
# This writing of (* args ) would be wrong manner.
# def all_total(*args , num): 
#     return sum(args)

# print(all_total(1,2,3,4))     # Here every number will be assign to the *args that is why it will throw error.    

# def all_total(*args):
#     mult=1
#     print(args)
#     for num in args:
#         mult*=num 
#     return mult

# nums=[1,2,3,4]
# print(all_total(*nums))   # Using (* here to unpack ) the list will work with tuple also.


# Exercise ............

# define a function
# input
# num , iterable(tuple , list)containing numbers as args

# example
# nums = [1,2,3]
# to_power(3, *nuns)

# output
# list ---> [1**3, 8, 27]

# if user didn't pass any args then give a user a message 'hey you did't pass
# args

# else
#return list


# def to_power(num,*args):
#     if args:
#         return [i**num for i in args]
#     else:
#         return "You did't pass anything"

# list=[1,2,3]
# print(to_power(3,*list))


# kwargs (keyword argument)
# **kwargs (double star operator)
# kwargs as a parameters

# def func(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

# func(first_name='Pankaj',last_name='Chauhan')

# def func(**kwargs):   # kwargs takes input as the dictionaries...  
#     for k,v in kwargs.items():
#         print(f"{k}:{v}")

# func(first_name='Pankaj',last_name='Chauhan')

# def func(name,**kwargs):                              # kwargs takes input as the dictionaries...  
#     print(name)
#     for k,v in kwargs.items():
#         print(f"{k}:{v}")

# func('anima',first_name='Pankaj',last_name='Chauhan')


# def func(name,**kwargs):                              # kwargs takes input as the dictionaries...  
#     print(name)
#     for k,v in kwargs.items():
#         print(f"{k}:{v}")
# d={'first_name':'pankaj' ,'last_name':'chauhan'}
# func('anima',**d)                                     # Using ** to unpack the dict......



# def func(name,*args ,last_name='chauhan',**kwargs):   # argument order 
#     print(name)
#     print(args)
#     print(last_name)
#     print(kwargs)

# func('pankaj',1,2,3,5,6,7,a=1,b=2)

# functions with all parameters
# very important to understand


# PADK                                                   # (Remember only PADK order will be maintain)

# parameters
# args
# default parameters
# kwargs

# def func(parameters,*args,last_name='unknown',**kwargs):
#     print(parameters)
#     print(args)
#     print(last_name)
#     print(kwargs)

# func('pankaj','chauhan','anima',3,2,4,a=2,b=6)


# Exercise ..
# def a function

# def func(l,**kargs):
#     if kargs.get('reverse_str')==True:
#         return [name[::-1].title() for name in l]


# names=['harshit','mohit']
# # print(func(*names))
# print(func(names,reverse_str=True))


# .................................Chapter 12 (Lambda Expression--> anonymous function)..............................

 
# def add(a,b):
#     return a+b

# add2=lambda a,b: a+b     # anonymous function 
# print(add2(4,5))

# multiply=lambda a,b :a*b
# print(multiply(6,7))

# Practice 

# is_even=lambda a:a%2==0
# print(is_even(8))

# last_char=lambda s:s[-1]
# print(last_char("pankaj"))

# Lambda with if ,else .. 

# func=lambda s:True if len(s)>5 else False
# print(func('pankaj')) 


# ........................................... Chapter 13 Enumerate function .......................................


# We use enumerate function with for loop to track position of our item in iterable

# How we can do this without enumerate function

# names=['abc','defghi','pankaj']
# pos=0
# for name in names:
#     print(f"{pos}--->{name}")
#     pos+=1

# with enumerate function

# for pos,name in enumerate(names):
#     print(f"{pos}-->{name}")
        
# Exercise ...

# Define a function that take two arguments
#1.) list containing string
# 2.) string , that want to find in your list
# and this function will return the index of string in your list and
# if string is not present then return -1

# def find(str,list):
#     ans=-1
#     for pos,name in enumerate(list):
#         if name==str:
#             ans=pos
#     return ans

# list=['anima','preety','radhika','punam']
# str='anima'
# print(find('punam',list))


# map function...

# numbers=[1,2,3,4]

# def square(a):
#     return a**2

# list=list(map(square,numbers))
# list=list(map(lambda a:a**2,numbers))
# print(list)


# Filter function..

# def is_even(a):
#     return a%2==0

# numbers=[4,3,2,1,5,6,9,8,10]  
# evens=tuple(filter(is_even,numbers))
# evens=tuple(filter(lambda a:a%2==0,numbers))
# print(evens)

# Iterator vs Iterable ..... (TASK FOR ME)

# Zip function....

# user_id=['user1','user2','user3']
# names=['pankaj','rohit','mohit']

#(user1,pankaj) (user2,rohit) (user3,mohit)

#print(list(zip(user_id,names))) #[('user1', 'pankaj'), ('user2', 'rohit'), ('user3', 'mohit')]

# user_id=['user1','user2']
# names=['pankaj','rohit','mohit']

# print(list(zip(user_id,names))) #[('user1', 'pankaj'), ('user2', 'rohit')]

# More about zip functions...

# l1=[1,3,5,7]
# l2=[2,4,6,8]

# l=[(1,2),(3,4),(5,6),(7,8)]

# l1,l2 = list(zip(*l))
# print(l1)
# print(l2)

# Exercise ...........................

# THIS IS CHALLENGE

# define a function take any no's of lists containing number.
# [1,2,3] , [4,5,6], [7,8,9]
# return average
# (1+4+7)/3 , (2+5+8)/3, (3+6+9)/3

# try to make this anonymous function in one line using lambda 


# def func(*args):
#     average=[]
#     for pair in zip(*args):
#         average.append(sum(pair)/len(pair))
#     return average

# similar of the above code ..

# func=lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]

# print(func([1,2,3],[4,5,6],[3,4,5]))


# any , all function in python ...

# number1=[2,4,6,8,10]
# number2=[1,2,3,4,5,6]

# evens1=[]
# for num in number2:
#     evens1.append(num%2==0)

# print(all([True,True,True,True])) ---> If the all value is true it will return 
# true else will return false.

# print(any(evens1)) --> It is use to check is any value is giving the answer is 
# True or not if true it will return true

# print(all([n%2==0 for n in number1]))

# Advance min and max ...

# numbers=[1,2,4,5,7]
# print(max(numbers))
# print(min(numbers))


# name=['Pankaj','mohit','ab']
# print(max(name,key=lambda item:len(item)))

# fruits=['grapes','mango','apple']
# fruits.sort()
# print(sorted(fruits))


# fruits=('grapes','mango','apple')
# print(sorted(fruits))


# fruits={'grapes','mango','apple'}
# print(sorted(fruits))

# guitars = [
# {'model': 'yamaha f310','price':8400},
# {'model': 'faith naptune', 'price':50000 },
# {'model': 'faith apollo venus','price': 35000},
# {'model': 'taylor 814ce', 'price': 450000}
# ]

# print(sorted(guitars,key=lambda d:d['price'],reverse=True))


# what are doc strings

# def func(a,b): 
#     ''' this is doc string that i'm writing into the colon'''
#     return a+b
 
# print(func.__doc__)
 

# how to write docstring

# print(len.__doc__)
# print(sum.__doc__)

# how to see doctrings
# what is help function

# print(help(sum))


# ............................................ Chapter 14 Decoraters ...............................................


# You have to have a complete understanding of functions,
# first class function / closures
# then finally we will learn about decorators

# def square(a):
#     return a*a

# s=square
# print(s(7))
# print(s.__name__)
# print(square.__name__)
# print(s)
# print(square)


# Pass function as a argument
# map
# def square(a):
#     return a**2

# l=[1,2,3,4]
# print(list(map(square,l)))

# def my_map(func,l):
#     ans=[]
#     for item in l:
#         ans.append(func(item))
#     return ans

# print(my_map(square,l))
# print(my_map(lambda a:a**3,l))

# def my_map2(func,l):
#     return [func(item) for item in l]

# print(my_map2(lambda a:a**3,l))


# def func_1(func):
#     def next():
#         print("Now it is printing !")
#         func()
#         print("last printing line !")
        
#     return next
    
# @func_1
# def kuchh():
#     print("Kuchh function is calling by the main !")
    
# kuchhBhi()



# Function returning function (Clouser).

# def outer_func():
#     def inner_func():
#         print('inside inner func !')
#     return inner_func

# var=outer_func()
# var()

# def outer_func2(msg):
#     def inner_func2():
#         print(f'message is {msg}')
#     return inner_func2

# var=outer_func2("hello there !")
# var()

# def to_power(x):
#     def calc_power(n):
#         return n**x
#     return calc_power

# cube=to_power(3)
# print(cube(5))
# square=to_power(2)
# print(square(4))

# Decorators- enhance the functionality of other functions...
  
# def decorator_function(any_function):
#     def wrapper_function():
#         print('this is awesome function ')
#         any_function()
#     return wrapper_function

# @decorator_function  # shortcut..
# def func1():
#     print('this is function 1')

# @decorator_function # shortcut.. this is use for shorcut try to use always 
# def func2():
#     print('this is function 2') 
 
# func1() 
# func1=decorator_function(func2)
# func1()

# def decorator_function(any_function):
#     def wrapper_function(*args,**kwargs):
#         print('this is awesome function ')
#         return any_function(*args,**kwargs)
#     return wrapper_function

# @decorator_function
# def func(a):
#     print(f'this is function with argument {a}')


import turtle
turtle.bgcolor("black")

squary = turtle.Turtle()
squary.speed(20)
squary.pencolor("red")
for i in range(400):
    squary.forward(i)
    squary.left(91)

# ....................................... Chapter 15 Object oriented programming (OOPS) ..............................


# This is very important to learn this.

# OBJECT ORIENTED PROGRAMMING

# COMMON TOPIC IN ALMOST ALL POPULAR PROGRAMMING LANGUAGES (PYTHON, C+, JAVA)
# WITH COMMON IDEA BUT WITH DIFFERENT SYNTAX

# 00P IS JUST A STYLE/WAY TO WRITE A CODE

# VERY HELPFUL IN CREATING REAL WORLD PROGRAMS

# WE WILL SEE OTHER ADVANTAGES WHEN WE WILL START LEARNING 0OP

# OBJECTIVES
# WHAT IS CLASS
# HOW TO CREATE AN CLASS
# WHAT Is INIT METHOD--->(constructor)
# WHAT ARE ATTRIBUTES, INSTANCE VARIABLES
# HOW TO CREATE OUR OBJECT


# class Person:
#     def __init__(self,first_name,last_name,age):
#         # instance variable.
#         print('Init method / Constructor get called !')
#         self.first_name=first_name
#         self.last_name=last_name
#         self.age=age

# p1=Person('Harshit','Chauhan',24)
# p2=Person('Anima','Gogoi',25)
# print(p1.first_name)

# Exercise ...
# Create a laptop class with attributes like brand name , model name , price
# create two objects/instance of your laptop class

# class Laptop:
#     def __init__(self,brand_name,model_name,price):
#         self.brand_name=brand_name
#         self.model_name=model_name
#         self.price=price

# dell=Laptop('Dell','se23',560000)
# acer=Laptop('Acer','sr45',780000)

# print(dell.brand_name)
# print(acer.brand_name)


# Instance Method...

# class Person:
#     def __init__(self,first_name,last_name,age):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.age=age

#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
    
#     def is_above_18(self):
#         return self.age>18

# p1=Person('Pankaj','Chauhan',24)
# p2=Person('Anima','Gogoi',10)

# print(p2.full_name())
# print(p2.is_above_18())


# Exercise ......


# class Laptop:
#     def __init__(self,brand_name,model_name,price):
#         self.brand_name=brand_name
#         self.model_name=model_name
#         self.price=price

#     def apply_discount(self,per):
#         dis=(int)(self.price*per)/100
#         return self.price-dis

# dell=Laptop('Dell','se23',560000)
# acer=Laptop('Acer','sr45',780000)


# print(dell.brand_name)
# print(acer.apply_discount(10))


# class variable
# circle
# area
# circum

# class Circle:
#     pi=3.14
#     def __init__(self, radius):
#         self.radius = radius

#     def calc_circunference(self):
#         return 2*Circle.pi*self.radius

# c1= Circle(4)
# print(c1.calc_circunference())
# print(c1.__dict__)


# class Laptop:
#     discount_percent=10
#     def __init__(self,brand_name,model_name,price):
#         self.brand_name=brand_name
#         self.model_name=model_name
#         self.price=price

#     def apply_discount(self):
#         dis=(int)(self.price*self.discount_percent)/100
#         return self.price-dis

# dell=Laptop('Dell','se23',560000)
# acer=Laptop('Acer','sr45',780000)
# acer.discount_percent=50 # Discount on particular laptop..
# print(dell.brand_name)
# print(acer.apply_discount())


# class Person:
#     count_instances=0
#     def __init__(self):
#         Person.count_instances+=1
        
# p1=Person()
# p2=Person()
# p3=Person() 

# print(Person.count_instances)


# class instances.
# class Methods 
# Difference between class methods and instance methods,

# class Person:
#     count_instances=0
#     def __init__(self):
#         Person.count_instances+=1

#     @classmethod
#     def count_instance(cls):
#         return f"You have created {cls.count_instances} instances of {cls.__name__} class"
    
        
# p1=Person()
# p2=Person()
# p3=Person() 

# print(Person.count_instance())


# Class Method as a constructor..

# class Person:
#     count_instances=0
#     def __init__(self,first_name,second_name,age):
#         Person.count_instances+=1
#         self.first_name=first_name
#         self.second_name=second_name
#         self.age=age
    
#     @classmethod
#     def from_string(cls,string):
#         first,last,age = string.split(',')
#         return cls(first,last,age)

#     @classmethod
#     def count_instance(cls):
#         return f"You have created {cls.count_instances} instances of {cls.__name__} class"
    
#     def full_name(self):
#         return f"{self.first_name} {self.second_name}"
        
# p1=Person('Pankaj','Chauhan')
# p2=Person('Anima','Gogoi')
# p3=Person.from_string('Anubhav,Srivsatava,24') 
# print(p3.full_name())


# Static method ............


# class Person:
#     count_instances=0
#     def __init__(self,first_name,second_name,age):
#         Person.count_instances+=1
#         self.first_name=first_name
#         self.second_name=second_name
#         self.age=age
    
#     @classmethod
#     def from_string(cls,string):
#         first,last,age = string.split(',')
#         return cls(first,last,age)

#     @classmethod
#     def count_instance(cls):
#         return f"You have created {cls.count_instances} instances of {cls.__name__} class"
    
#     @staticmethod
#     def hello():
#         return "Hi guys static method called !"

#     def full_name(self):
#         return f"{self.first_name} {self.second_name}"
        
# p1=Person('Pankaj','Chauhan',45)
# p2=Person('Anima','Gogoi',67)
# p3=Person.from_string('Anubhav,Srivsatava,24') 
# print(p3.full_name())

# print(Person.hello()) 



# In this video we will talk about
# Encapsulation
# Abstraction
# Some special naming convention
# Name Mangling |


# class Phone:
#      def __init__ (self, brand,model_name, price):
#         self.brand = brand
#         self.model_name = model_name
#         self._price = max(price,0)
#         self.complete_specification=f"{self.brand} {self.model_name} and the price is {price}"

#      def make_a_call(self, phone_number):
#         print ("calling {phone_number} ...")

#      def fullpname(self):
#         return f"{self.brand} {self.model_name}" 
     
#      def send_message(self):
#          pass
     
# _name -->Convention is used for the private (but everthing in python is public)
# __name__ dunder/magic methods .

# phone1=Phone('Nokia','1100',-1000)
# phone1._price=600
# print(phone1._price)
# print(phone1.complete_specification)
# print(phone1.__dict__)






# inheritance in python .....

# class Phone:
#    def __init__(self,brand,model_name,price):
#       self.brand=brand
#       self.model_name=model_name
#       self._price=price

#    def full_name(self):
#       return f"{self.brand} {self.model_name}"

#    def make_a_call(self,number):
#       return f"calling{number}"



# class Smartphone(Phone):
#    def __init__(self,brand,model_name,price,ram ,internal_momory,rear_camera):
#       # Phone.__init__(self,brand,model_name,price)  # uncommon ways.
#       super().__init__(brand,model_name,price)   # don't need to write self...
#       self.ram=ram 
#       self.internal_memory=internal_momory
#       self.rear_camera=rear_camera


# phone1=Phone('nokia','1100',1000)
# smartphone=Smartphone('noeplus','s',30000,'6 GB','64 GB','20 MP')
# print(phone1.full_name())
# print(smartphone.full_name())



# Can we derive moer then one class from base class..
# Multilevel Inheritance
# Method resolution order
# Method overriding
# isinstance() ,issubclass()


# class Phone:
#    def __init__(self,brand,model_name,price):
#       self.brand=brand
#       self.model_name=model_name
#       self._price=price

#    def full_name(self):
#       return f"{self.brand} {self.model_name}"

#    def make_a_call(self,number):
#       return f"calling{number}"



# class Smartphone(Phone):
#    def __init__(self,brand,model_name,price,ram ,internal_momory,rear_camera):
#       # Phone.__init__(self,brand,model_name,price)  # uncommon ways.
#       super().__init__(brand,model_name,price)   # don't need to write self...
#       self.ram=ram 
#       self.internal_memory=internal_momory
#       self.rear_camera=rear_camera

# class Smartphone2(Phone):
#    def __init__(self,brand,model_name,price,ram ,internal_momory,rear_camera):
#       # Phone.__init__(self,brand,model_name,price)  # uncommon ways.
#       super().__init__(brand,model_name,price)   # don't need to write self...
#       self.ram=ram 
#       self.internal_memory=internal_momory
#       self.rear_camera=rear_camera


# phone1=Phone('nokia','1100',1000)
# smartphone=Smartphone('noeplus','s',30000,'6 GB','64 GB','20 MP')
# print(smartphone.full_name())
# print(phone1.full_name())



# Multiple inheritance .............

# class A:
#    def class_a_method(self):
#         return 'I\'m just class a method'
#    def hello(self):
#        return 'hello from class A'

# class B:
#    def class_b_method(self):
#         return 'I\'m just class A method'
#    def hello(self):
#        return 'hello from class B'

# class C(A,B):
#     pass


# instance_c=C()
# print(instance_c.class_a_method())
# print(instance_c.class_b_method())
# print(instance_c.hello())
# print(help(C))
# print(C.mro())


# special magic methods / dunder methods
# operator overloading
# polymorphism

# class Phone:
#    def __init__(self,brand,model,price):
#       self.brand=brand
#       self.model=model
#       self.price=price
#    def phone_name(self):
#       return f"{self.brand} {self.price}"
   
   # str ,repr

   # def __repr__(self) -> str:
   #    return f"{self.brand} {self.price}"
   
   # def __str__(self) -> str:
   #    return f"{self.brand} {self.price}"

   # def __repr__(self) -> str:
   #    return f"Phone(\'{self.brand}\',\'{self.model}\',{self.price})"



# l=[1,2,3,4]
# print(l)

# phone1=Phone('Nokia','1100',1200)
# print(phone1)



# Chapter 17 Built In errors .................................................................

# Built in errors
# Exception , how to handle them 
# raise your own error, debugging , etc etc..

# Syntax error...

# def func()
#    pass
# name='Pankah'*

# Indendation error..
# def func():
#     print('hello')
#   print('world')

# variable name error ..
# print(name)

# Type error...
# print(5+'pankaj')

# index error.
# l=[1,2,3]
# print(l[4])

# value error
# s='abc'
# print(int(s))

# Attribute error...
# l=[1,2,3]
# l.push(6)  # there is no any attribut in python called push 
# print(l)

# key error...
# d={'name':'harshit'}
# print(d['age'])

# raise ...

# def func(a,b):
#    if(type(a) is int and type(b) is int):
#         return a+b
#    raise TypeError("OOPs you are not passing the integer to the function !")

# print(func(2,'3')) 

# raise example error 1
# NotImplementedError
# abstract method 

# class Animal:
#    def __init__(self,name):
#       self.name=name
#    def sound(self):
#       raise NotImplementedError("You have not define this method into the subclass !")

# class Dog(Animal):
#    def __init__(self,name,breed):
#       super().__init__(name)
#       self.breed=breed

#    def sound(self):
#       return "Bhow Bhow !"

# class Cat(Animal):
#    def __init__(self, name,breed):
#       super().__init__(name)  
#       self.breed=breed

#    def sound(self):
#       return "meao meao !"

# doggy=Dog('boony','pug')
# print(doggy.sound())


# error raise example 2.

# class Mobile:
#     def __init__(self,name):
#         self.name=name
   
# class MobileStore:
#    def __init__(self):
#       self.mobiles=[]

#    def add_mobile(self,new_mobile):
#       if isinstance(new_mobile,Mobile):
#          self.mobiles.append(new_mobile)
#       else:
#          raise TypeError('New mobile should be object of Mobile class !')

# oneplus=Mobile('one plus 6')
# samsung='samsung galaxy s8'
# mobo_store=MobileStore()
# # print(mobo_store.mobiles)
# mobo_store.add_mobile(oneplus)
# print(mobo_store)
   
# Exception handling .....
# try except else finally 

# age =int(input('enter your age !'))
# if age<18:
#     print('you can\'t play this game !')
# else:
#     print('probably you can play now !')       

# while True:
#    try:
#       age =int(input('enter your age : '))
#       break 
#    except ValueError:           # this is like airthmetic 
#       print('Invalid Input :')
#    except:                      # this is like parent class 
#       print('Unexpected error !')

# if age<18:
#     print('you can\'t play this game !')
# else:
#     print('probably you can play now !')       


# else and finally clause in exceptio handling ........

# while True:
#    try:
#       age =int(input('enter your age : ')) 
#    except ValueError:           # this is like airthmetic 
#       print('Invalid Input :')
#    except:                      # this is like parent class 
#       print('Unexpected error !')
#    else:
#       print(f'user input ={age}')
#       break
#    finally:
#       print('This will always run in any situation !(Because this is finally block)')

# Exercise ...

# make a function divide 
# divide (a,b)
# print(divide(4,2)) # 2
# print(divide(4,0)) # Don't divide with zero 
# print(divide('4',2)) # Please input numbers only .


# def divide(a,b):
#    try:
#       return a/b
#    except ZeroDivisionError as err:
#       print(err)
#    except TypeError as err:
#       print('Please enter the number only !')
#    except:
#       print('Unexpected error !')

# print(divide('r',2))

# python custom exception...
# Q- why custom exceptions ..
# A -To increase the readiblity of code ...

# Example ..

# class NameTooShort(ValueError):
#     pass

# def Validate(name):
#     if len(name)<8:
#         raise NameTooShort('name is too short')
   
# username=input('Enter your name: ')
# Validate(username)
# print(f'hello {username}')
# NameTooshort


