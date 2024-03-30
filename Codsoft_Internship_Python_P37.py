#!/usr/bin/env python
# coding: utf-8

# ## 1. Calculator

# #### Task: Designing a simple calculator with basic arithmetic operations.

# #### #1 Using if else statement

# In[3]:


arthmetic_operator= input('Enter an operator of your choice(+ - * /): ')
val1= float(input(' Enter the first value: '))
val2= float(input(' Enter the second value: '))

if arthmetic_operator == '+':
    result= val1 + val2
    print(round(result, 2))
elif arthmetic_operator == '-':
    result= val1 - val2
    print(round(result, 2))
elif arthmetic_operator == '*':
    result= val1 * val2
    print(round(result, 2))
elif arthmetic_operator == '/':
    result= val1 / val2
    print(round(result, 2))
else:
    print(f"{arthmetic_operator} is invalid, enter a valid operator")


# In[4]:


arthmetic_operator= input('Enter an operator of your choice(+ - * /): ')
val1= float(input(' Enter the first value: '))
val2= float(input(' Enter the second value: '))

if arthmetic_operator == '+':
    result= val1 + val2
    print(round(result, 2))
elif arthmetic_operator == '-':
    result= val1 - val2
    print(round(result, 2))
elif arthmetic_operator == '*':
    result= val1 * val2
    print(round(result, 2))
elif arthmetic_operator == '/':
    result= val1 / val2
    print(round(result, 2))
else:
    print(f"{arthmetic_operator} is invalid, enter a valid operator")


# #### #2 Using user defined

# In[8]:


def calculator(operator, x, y):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == '/':
        if y != 0:
            return x / y
        else:
            return "Not allowed"
    else:
        return "Invalid operator"

print("Select operator:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

user_input = input("Enter your choice (+/-/*/): ")

num1 = float(input("Enter first value: "))
num2 = float(input("Enter second value: "))

if user_input in ['+', '-', '*', '/']:
    print("Result:", calculator(user_input, num1, num2))


# In[ ]:





# ## 2. Password generator

# #### Task: Prompting the user to specify the desired length of the password, Using a combination of random characters to generate a password of the specified length

# #### #1 

# In[11]:


import string
import random

user_input= input('Do you want to generate a password? Yes/No: ')
if user_input == 'Yes':
    generate_password()
elif user_input == 'No':
    print('Thank You!')
else:
    print('Invalid Input')
    

characters = list(string.ascii_letters + string.digits + "@#$*()%!")

def generate_password():
    password_length = int(input('Enter the length of your password: '))
    random.shuffle(characters)
    
    password= []
    
    for x in range(password_length):
        password.append(random.choice(characters))
        
    random.shuffle(password)
    
    password = "".join(password)
    print(password)
    


# __The error is occuring as we have defined our 'generate_password' after the entire 'user_input'
# if we switch the order it might work. So, let's check that.__

# In[12]:


import string
import random


characters = list(string.ascii_letters + string.digits + "@#$*()%!")

def generate_password():
    password_length = int(input('Enter the length of your password: '))
    random.shuffle(characters)
    
    password= []
    
    for x in range(password_length):
        password.append(random.choice(characters))
        
    random.shuffle(password)
    
    password = "".join(password)
    print(password)
    
user_input= input('Do you want to generate a password? Yes/No: ')
if user_input == 'Yes':
    generate_password()
elif user_input == 'No':
    print('Thank You!')
else:
    print('Invalid Input')


# __It works just fine. Yay!!__

# #### #2

# In[14]:


import string
import random

def random_password(length):
    characters = string.ascii_letters + string.digits + "@#$*()%!"
    password = ''.join(random.choice(characters) for i in range(length))
    return password

length = int(input("Enter the length of the password: "))
print("Your generated password is:", random_password(length))


# In[ ]:





# ## 3. Quiz game

# #### Task: Creating a quiz game that asks users multiple choice questions on specific topic

# In[23]:


def new_game():
    guess= []
    correct_guess = 0
    question_num =1
    
    for key in questions:
        print('********************')
        print(key)
        for x in options[question_num - 1]:  #-1 as it always starts with 0
            print(x)
        user_guess = input('Enter (A, B, C or D): ')
        user_guess= user_guess.upper()  #so that if user inputs a instead of A
        guess.append(user_guess)
        
        correct_guess += check_answer(questions.get(key), user_guess)
        question_num += 1
        
    display_score(correct_guess, user_guess)

# -----------------------------------------------------------------------------------------------------

def check_answer(answer, user_guess):
    if answer == user_guess:
        print('Correct')
        return 1
    else:
        print('Oops! Wrong')
        return 0
    
# -----------------------------------------------------------------------------------------------------

def display_score(correct_guess, user_guess):
    print('*********************************')
    print('Results')
    print('*********************************')
    
    print('Answers: ', end= '')
    for x in questions:
        print(questions.get(x), end = ' ')
        
    print('user_guess: ', end= '')
    for x in user_guess:
        print(x, end = ' ')
    print()
    
    score= int((correct_guess/len(questions))*100)
    print("You've scored: " + str(score) + '%' )
        
# -----------------------------------------------------------------------------------------------------

questions = {'Which is the largest coffee-producing state of India?: ' : 'C',
            'The most powerful prime minister in the world?: ' : 'B',
            'Which Girl group is from South Korea?: ' : 'A',
            'Who is the autjor of Pride and Prejudice?: ' : 'D'
           }

options = [['A. West Bengal', 'B. Tamil Nadu', 'C. Karnataka', 'D. Assam'],
          [' A. Vladimir Putin', 'B. Narendra Modi', 'C. Joe Biden', 'D. Shehbaz Sharif'],
          ['A. Red Velvet', 'B. W.I.S.H', 'C. Nogizaka46', 'D. DOLLA'],
          ['A. Emily Bronte', 'B. Robert Frost', 'C. Virginia Woolf', 'D. Jane Austen']]

new_game()


# In[ ]:




