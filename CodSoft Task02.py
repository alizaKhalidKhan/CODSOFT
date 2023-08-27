#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Internship @CodSoft - Task (2)
"""Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result.
"""

class calculator:  #A class that defines all the basic operations of a calculator
    
    def addition(self,number_1,number_2): #Takes two arguments: Number 1 and 2
        return number_1+number_2   #Will return the result of two numbers after addition
    
    def subtraction(self,number_1,number_2): #Takes two arguments: Number 1 and 2
        return number_1-number_2  #Will return the result of two numbers after subtraction
    
    def multiplication(self,number_1,number_2): #Takes two arguments: Number 1 and 2
        return number_1*number_2  ##Will return the result of two numbers after multiplication
    
    def division(self,number_1,number_2): #Takes two arguments: Number 1 and 2
        if number_2 == 0:       #If number_2 is 0 then it will be an error           
            return "Math Error: Cannot Divide the number by ZERO"
        return number_1/number_2 #If number_2 is not 0 then this statement will execute
    
def display_Menu():   #A class that defines the menu
    print("Select The operation (1-5)") 
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Quit") #printing the menu
    Menu_Choice=int(input("Enter from Menu(1-5)")) #Taking input from user
    return Menu_Choice

calc=calculator() #Creating object of class "calculator"
while True:
    Menu_Choice=display_Menu()
    number_1=float(input("Enter Number:1  "))
    number_2=float(input("Enter Number:2  "))
    if Menu_Choice==1:
        print(calc.addition(number_1,number_2))
        
    elif Menu_Choice==2:
        print(calc.subtraction(number_1,number_2))
    
    elif Menu_Choice==3:
        print(calc.multiplication(number_1,number_2))
        
    elif Menu_Choice==4:
        print(calc.division(number_1,number_2))
        
    elif Menu_Choice==5:
        print("Quitting.....")
        break
    else:
        print("Invalid Choice: Try Again!")
        
    repeat = input("\nDo you want to perform another operation? (Y/N): ")
    if repeat.upper() == "N":
        print("Quitting the program...")
        break


# In[ ]:




