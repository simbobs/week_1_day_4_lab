tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

# def get_uncompleted_tasks(list):
#     uncompleted_tasks = []
#     for task in list:
#         if task["completed"] == False:
#             uncompleted_tasks.append(task["description"])
#     return uncompleted_tasks

# print(get_uncompleted_tasks(tasks))

# def get_completed_tasks(list):
#     completed_tasks = []
#     for task in list:
#         if task["completed"] == True:
#             completed_tasks.append(task["description"])
#     return completed_tasks

# print(get_completed_tasks(tasks))

# def get_tasks_taking_at_least(list,time):
#     task_time = None
#     for task in list:
#         if task["time_taken"] == time:
#             task_time = task["description"]
    
#     return task_time
  
# print(get_tasks_taking_at_least(tasks,10))         
        
# def get_task_with_description(list, description):
#     found_task_name = None
#     for task in list:
#         if task["description"] == description:
#             found_task_name = task
            
#     return found_task_name

# print(get_task_with_description(tasks,"Walk Dog"))

def get_tasks_by_status(list, status):
    task_status = []
    for task in list:
        if task["completed"] == status:
            task_status.append(task["description"])
    return task_status
        
  
print(get_tasks_by_status(tasks, True))
      
