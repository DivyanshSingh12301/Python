# Q3 : Seconds converter
# Write a program that takes a number of seconds as input and converts it to hours, minutes, and seconds.
# seconds = int(input("Enter the number of seconds: "))
# hours = seconds // 3600
# minutes = (seconds % 3600) // 60
# seconds = seconds % 60
# print(f"{hours} hours, {minutes} minutes, {seconds} seconds")

# Q4
# print("Enter your age: ")
# year = int(input("Enter total years:"))
# total_days = year * 365;
# print(f"You have lived for approximately {total_days} days.")
# hours = total_days * 24
# print(f"You have lived for approximately {hours} hours.")
# minutes = hours * 60
# print(f"You have lived for approximately {minutes} minutes.")

#Q2 : A BMI Calculator.
# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in meters: "))
# bmi = weight / (height ** 2)
# print(f"Your BMI is: {bmi:.2f}")

# print(5>3)

#Q2 : A BMI Calculator.
# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in meters: "))
# bmi = weight / (height ** 2)
# print(f"Your BMI is: {bmi:.2f}")
# if bmi < 18.5:
#     print("You are underweight.")
# elif 18.5 <= bmi < 24.9:
#     print("You are normal weight.")
# elif 25 <= bmi < 29.9:
#     print("You are overweight.")
# else:
#     print("You are obese.")

# # Chapter 2 : 
# # Q1
# correct_username = "Divyansh"
# correct_password = "python123"
# password = input("Enter your password: ")
# username = input("Enter your username: ")
# if username == correct_username and password == correct_password:
#     print("Login successful!")
# elif username == correct_username and password != correct_password:
#     print("Incorrect password.")
# else :
#     print(" User not found.")

# Improved version of above code
# correct_username = "Divyansh"
# correct_password = "python123"
# username = input("Enter username: ")
# password = input("Enter password: ")
# if username == correct_username and password == correct_password:
#     print("Login successful!")
# elif username == correct_username:
#     print("Incorrect password.")
# else:
#     print("User not found.")

# Q2 : Improved version using loops
# correct_username = "Divyansh"
# correct_password = "python123"
# while True:
#     username = input("Enter username: ")
#     password = input("Enter password: ")
#     if username == correct_username and password == correct_password:
#         print("Login successful!")
#         break
#     else:
#         print("Invalid username or password.")  

# Q3
# secret_number = 7
# attempts=0
# while True:
#     attempts += 1
#     guess = int(input("Guess the number between 1 and 10: "))
#     if guess == secret_number:
#         print(f"Congratulations! You guessed the number in {attempts} attempts.")
#         break
#     else:
#         print("Try again.")

# from random import randint
# print("""Welcome to the Number Guessing Game!
# I have chosen a number between 1 and 100.
# You have 7 attempts to guess it.""")
# random_number = randint(1, 100)
# state = False
# for i in range(1,8):
#     guess =  int(input("Guess the number between 1 and 100: "))
#     if guess == random_number:
#         print(f"Congratulations! You guessed the number in {i} attempts.")
#         state = True
#         break
#     elif guess < random_number:
#         print("Too low!.")
#         print(f"You have {7-i} attempts left.")
#     else:
#         print("Too high!")
#         print(f"You have {7-i} attempts left.")

# if not state:
#     print(f"Sorry, you've used all your attempts. The number was {random_number}.")      

# Numbers from 1 to 20 except those which are divisible by 3
# for i in range(1,21):
#     if i % 3 == 0:
#         continue
#     print(i)

    
# def add(a,b):
#     print(a+b)
# result = add(5,10)
# print(result)

# import random
# def generate_number():
#     random_number = random.randint(1,100)
#     return(random_number)
# def check_guess(guess,secret):
#     if guess == secret:
#         return "Correct"
#     elif guess > secret:
#         return"Too High"
#     else:
#         return "Too Low"
   
# def play_game():
#     print("WELCOME")
#     a = generate_number()
#     state = False 
#     for i in range(1,8):
#        while True:
#         try:
#           b = int(input("Guess a number between 1 and 100: "))
#           break
#         except:
#           print("Enter numbers only")
#           continue
#        checking = check_guess(b,a)
#        print(checking)
#        if checking == "Correct":
#            print("You won")
#            state = True
#            break
#        print(f"You have {7-i} attempts left")
#     if not state:
#             print(f"You Lost: The number was {a}")
# play_game()


# task = []
# print("Choose 1 to add task, 2 to remove task, 3 to show task and 4 to exit task.")
# while True:
#   choice = int(input("Choose: "))
#   if choice == 1 :
#     your_choice = input("Enter task: ")
#     task.append(your_choice)
#     print("Added")
#   elif choice == 2:
#     your_choice = input("Enter what you want to remove: ")
#     task.remove(your_choice)
#     print("Remove")
#   elif choice == 3:
#     print("Your tasks are: ")
#     for tasks in task:
#         print(task)
#   elif choice == 4:
#       print("Exit")
#       break
  
  
# tasks = []
# while True:
#     print("""===== TO DO LIST =====

# 1. Add task
# 2. Remove task
# 3. Show tasks
# 4. Mark task as completed
# 5. Exit

# Choose:""")
#     try:
#      choice = int(input(""))
     
#     except:
#       print("Enter a valid number")
#       continue
    
#     if choice == 1 :
#      your_choice = input("Enter task: ")
#      tasks.append(your_choice)
#      print("Task Added successfully")
#     elif choice == 2 :
#      if len(tasks) == 0:
#          print("You have zero tasks")
#          print("Add a task first") 
#      else:       
#       print("Your tasks: ")
#       for index, task in enumerate(tasks,start = 1):
#         print(f"{index}. {task}")
#       try:
#        your_choice = int(input("Enter task number to remove: "))
#       except:
#        print("Enter a valid number")  
#       if your_choice > len(tasks):
#          print("Invalid task number.")
#       else:   
#        tasks.pop(your_choice - 1)
#        print("Task removed")
#     elif choice == 3:
#      if len(tasks) == 0:
#        print("No tasks available")
#      else:
#       print("Your tasks: ")  
#       for index, task in enumerate(tasks,start = 1):
#          print(f"{index}. {task}")
#     elif choice == 4:
#       print("Your tasks: ")
#       for index, task in enumerate(tasks,start = 1):
#         print(f"{index}. {task}")  
#       print("Which task completed? ")
#       task_completed = int(input())  
#       if task_completed > len(tasks):
#           print("Invalid task number.")
#       else:   
#        tasks[task_completed - 1] = tasks[task_completed - 1] + "✅"
#     elif choice == 5:
#       print("Goodbye")    
#       break
#     else:
#         print("Invalid")
#         print("Please choose between 1 and 5 ") 
  
# # Final project chapter 4 - An inventory

# inventory = []
# while True:
#     print("""===== INVENTORY =====

# 1. Add item
# 2. Remove item
# 3. Search item
# 4. Show inventory
# 5. Sort inventory
# 6. Exit""")
#     try:
#         choice = int(input("Choose: "))
#     except:
#         print("Enter a valid number")
#         continue
#     if choice == 1:
#         your_choice = input("Enter item: ").lower()
#         inventory.append(your_choice)
#         print("Item added successfully")
#     elif choice == 2:
#         if len(inventory) == 0:
#             print("Inventory has zero items")
#             continue
            
#         your_choice = input("Enter which item you wanna remove: ")
#         if your_choice in inventory:
#             inventory.remove(your_choice)
#             print("Removed")
#         else:
#             print("Item not found")
#     elif choice == 3:
#         your_choice = input("Enter item that you wanna search: ").lower()
#         if your_choice in inventory:
#             print(f"{your_choice} is in inventory")
#         else:
#             print("Item not found")
#     elif choice == 4:
#         if len(inventory) == 0:
#             print("Inventory is empty")
#         else:
#             for index, items in enumerate(inventory, start = 1):
#                 print(f"{index}. {items}")
#     elif choice == 5:
#         if len(inventory) == 0:
#             print("Inventory is empty")
#         else:
#             inventory.sort()
#             print("Inventory sorted successfully")
#     elif choice == 6:
#         print("Exit")
#         break
#     else:
#         print("Enter a valid choice")
                                           
    

# Character battle game
# player = {
#     "name": "Knight",
#     "health": 100,
#     "attack": 20,
#     "potions": 3
# }

# enemy = {
#     "name": "Goblin",
#     "health": 80,
#     "attack": 15
# }
# print("""⚔️ Knight VS Goblin ⚔️

# Knight HP: 100
# Goblin HP: 80
# """)
# while True:
#     print("""Choose:

# 1. Attack
# 2. Heal
# 3. Run
# """)
#     choice = int(input())
#     if choice == 1:
#          print("You attacked Goblin for 20 damage")
#          enemy["health"] = enemy["health"] - 20
#          if enemy["health"] <= 0:
#             print("You defeated the goblin")
#             print(f"Your health is {player['health']}")
#             break
#          print("Now the enemy attacks")
#          print("Goblin attacked you for 15 damage")
#          player["health"] = player["health"] - 15
#          if player["health"] <= 0:
#             print("You lost")
#             print(f"Enemy's health was {enemy['health']}")
#             break
#          print(f"Goblin's health is {enemy['health']}")
#          print(f"Your health is {player['health']}")
        
#     elif choice == 2:
#         if player["potions"] > 0:
#             player["health"] = player["health"] + 30
#             player["potions"] = player["potions"] - 1
#         else:
#             print("Not enough portions")
#     elif choice == 3:
#         print("Game ended")
#         break
#     else:
#         print("Enter a valid option")
        
        
# strin = ["AB" , "CD"]
# print(strin)        


# Password Strength Checker
# print("""Create your password.

# Rules:
# 1. Minimum 8 characters
# 2. Must contain an uppercase letter
# 3. Must contain a lowercase letter
# 4. Must contain a number

# Enter password:
# """)

# while True:
#     password = input()
#     if len(password) < 8:
#         print("Weak password (Must be at least 8 characters)")
#         print("Try again\n")
#         continue
#     has_upper = False
#     has_lower = False
#     has_digit = False

#     for char in password:
#         if char.isupper():
#             has_upper = True
#         elif char.islower():
#             has_lower = True
#         elif char.isdigit():
#             has_digit = True
#     if not has_upper:
#         print("Weak password (Missing an uppercase letter)")
#         print("Try again\n")
#         continue
#     elif not has_lower:
#         print("Weak password (Missing a lowercase letter)")
#         print("Try again\n")
#         continue
#     elif not has_digit:
#         print("Weak password (Missing a number)")
#         print("Try again\n")
#         continue
   
#     print("Strong password")
#     break


# Text Cleaner Bot 🤖
# sentence = "    I love Java because Java is easy    "
# new_sentence = sentence.strip()
# replace_sentence = new_sentence.replace("Java", "Python")
# lists_sentence = replace_sentence.split()
# string_sentence = "-".join(lists_sentence)
# print("Clean sentence:")
# print(f"{replace_sentence}\n")
# print("Words:")
# print(f"{lists_sentence}\n")
# print("Word count:")
# print(f"{len(lists_sentence)}\n")
# print("Joined:")
# print(string_sentence)


# # Creating a Contact Extractor
# import re
# text = """
# My phone is 9876543210.
# Office number: 9123456789.
# Email me at test@gmail.com
# """

# numbers = re.findall(r"\d{10}",text)
# print("Numbers:")
# print(numbers)
# email_regex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
# extracted_emails = email_regex.findall(text)
# print("Emails:")
# for email in extracted_emails:
#     print(email)