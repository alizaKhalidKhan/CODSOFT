#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Internship @CodSoft - Task (3)

"""A To-Do List application is a useful project that helps users manage
and organize their tasks efficiently. This project aims to create a
command-line or GUI-based application using Python, allowing
users to create, update, and track their to-do lists"""

#Interface Used In Below Program : Command Line Interface
#Program : Menu-Driven Program
#Data Structure Used : Linked List

class Todo_Tasks:
    
    def __init__(self,name):
        
        """
        Represents a task with its name.

        Args:
            name (str): The name of the task.
        """
        
        self.name = name
        self.completed = False
        self.next = None

class To_Do_List:
    
    """
    
    To do list class handles the addition, displaying, searching, updation and deletion of tasks.
    
    """
    def __init__(self):
        
        self.head=None
    
    def addTask(self,task_name):
        
        """
        Adds a contact to the contact book.
        
        Args:
            task_name (str): The name of the task to be added.
        """
        
        new_task = Todo_Tasks(task_name)
        if self.head is None:
            self.head = new_task
        else:
            curNode=self.head
            while curNode.next is not None:
                curNode = curNode.next
            curNode.next=new_task
        print("Task added succesfully in to-do-list!")
    
    def deleteTask(self, task_name):
                        
        """
        Deletes a task from the to-do-list.
        
        Args:
            task_name (str): The name of the task to be deleted.
        """
        
        if self.head is None:
            print("No tasks to delete!")
            return
        
        if self.head.name==task_name:
            self.head = self.head.next
            print("Task deleted successfully!")
            return
        
        curNode = self.head
        prev = None
        while curNode:
            if curNode.name==task_name:
                prev.next=curNode.next
                print("Task deleted succesfully!")
                return
            prev=curNode
            curNode=curNode.next
        print("Task not found!")
        
    def searchTask(self, task_name):
        
        """
        Searches for a task in the to-do-list.

        Args:
            task_name (str): The name of the task.
        """
        
        curNode = self.head
        while curNode:
            if curNode.name==task_name:
                return curNode
            curNode=curNode.next
        return None
    
    def displayTasks(self,show_completed=False):
        
                 
        """
        
        Displays all the tasks in the in the to-do-list.
        
        """
        
        if self.head is None:
            print("No tasks to display")
            return
        
        curNode = self.head
        while curNode:
            if show_completed or not curNode.completed:
                status = "Completed" if curNode.completed else "Not Completed"
                print(f"Task: {curNode.name} - Status: {status}")
            curNode = curNode.next

    def mark_completed(self, task_name):

        """
        Marks a task complete in the to-do-list.

        Args:
            task_name (str): The name of the task.
        """
        
        task = self.searchTask(task_name)
        if task:
            task.completed = True
            print("Task marked as completed!")
        else:
            print("Task not found!")
            
    def display_completed_tasks(self):
        """
        Displays all the completed tasks in the to-do-list.
        """
        if self.head is None:
            print("No tasks to display")
            return
        
        curNode = self.head
        while curNode:
            if curNode.completed:  # Only display completed tasks
                print(f"Task: {curNode.name} - Status: Completed")
            curNode = curNode.next
            
todo_list = To_Do_List()

while True:
        print()
        print("To-Do List Menu")
        print("1. Add Task")
        print("2. Display Task")
        print("3. Search Task")
        print("4. Delete Task")
        print("5. Mark Complete")
        print("6. Display Completed Tasks")
        print("7. Quit")
        print()
        
        choice = int(input("Enter your choice: (1-7)  "))
        
        if choice == 1:
            task_name = input("Enter the task name: ")
            todo_list.addTask(task_name)
        
        elif choice == 2:
            todo_list.displayTasks()
            
        elif choice == 3:
            task_name = input("Enter the task name to search: ")
            task = todo_list.searchTask(task_name)
            if task:
                status = "Completed" if task.completed else "Not Completed"
                print(f"Task found: {task.name} - Status: {status}")
            else:
                print("Task not found!")
                
        elif choice == 4:
            task_name = input("Enter the task name to delete: ")
            todo_list.deleteTask(task_name)
            
        elif choice == 5:
            task_name = input("Enter the task name to mark it as completed: ")
            todo_list.mark_completed(task_name)
            
        elif choice == 6:
            todo_list.display_completed_tasks()   
            
        elif choice == 7:
            print("Quitting the program....")
            break
            
        else:
            print("Invalid Input")
            print("Try Again!")
            continue


# In[ ]:




