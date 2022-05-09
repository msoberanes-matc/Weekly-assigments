#!/usr/bin/env python3
import json
import requests
import argparse


parser = argparse.ArgumentParser(description='Python Scripting Final')

parser.add_argument('-u'                   
                    , dest='id'
                    , metavar="[user ID]"
                    , type=int, required=True
                    , help='Enter a user ID')

parser.add_argument('-c'
                    , dest='varBool'
                    , default=False
                    , action='store_true'
                    , help='Include this flag if you want to see number of completed tasks')

args = parser.parse_args()

def check_varBool():
    bool_flag =  args.varBool
    return bool_flag
    
bool_flag = check_varBool()
#print(bool_flag)

def check_user_id():
    input_id =  args.id
    return input_id
    
input_id = check_user_id()

valid_id = input_id
users_id = (args.id -1)
alto = "no"

if valid_id == 0:
    print("Cannot use that user ID")
    alto = "yes"
if valid_id <= 10:
    alto = "no"
else:
    print("Cannot use that user ID")
    alto = "yes"
        
url_users = "https://jsonplaceholder.typicode.com/users"
response_u = requests.get(url_users)
users = json.loads(response_u.text)

url_todos = "https://jsonplaceholder.typicode.com/todos"
response_t = requests.get(url_todos)
tasks = json.loads(response_t.text)

if alto!= "yes":
     
    rango = 0    
    count = 0
    if valid_id == 1:
        rango = 0
    elif valid_id == 2:
        rango = 20    
    elif valid_id == 3:
        rango = 40
    elif valid_id == 4:
        rango = 60    
    elif valid_id == 5:
        rango = 80
    elif valid_id == 6:
        rango = 100    
    elif valid_id == 7:
        rango = 120
    elif valid_id == 8:
        rango = 140    
    elif valid_id == 9:
        rango = 160
    elif valid_id == 10:
        rango = 180    
      
                  
    completed = 0
   
    not_completed = 0
    
    
    for key in tasks:
            
        tasks_id = json.dumps(tasks[rango]["userId"])
        tasks_id_int = int(tasks_id)
                    
        if valid_id == tasks_id_int:
                                   
            if json.dumps(tasks[rango]["completed"]) == "true" : 
                completed += 1 
            else:
                not_completed += 1
         
            if bool_flag != True:
                print(f"User {json.dumps(users[users_id]['name'])} has to complete {not_completed} tasks")
            else:
                print(f"User {json.dumps(users[users_id]['name'])} has {completed} tasks completed and {not_completed} to do")              
        else:
            break
            
        rango += 1 
    

            
          
