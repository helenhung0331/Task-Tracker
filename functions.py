import json
from datetime import datetime

from task import Task

filename = 'tasks.json'
add_filename = 'add_count.txt'

def add_task(message):
    description = message[13:]
    if description.startswith('"') and description.endswith('"'):
        description = description[1:-1]
        if description != '':
        
            with open(add_filename) as f:
                count = f.read()
                if count == '\n':
                    count = 0
                else:
                    count = int(count)
        # what if the file even does not exist? remaining questions...
        # read json file from tasks.json and get the data_list
            new_task = Task(description)
            new_task.id = count + 1
        # new_task.id = length of data_list + 1
            data = {
                'id': new_task.id, 
                'description': new_task.description, 
                'status': new_task.status,
                'createdAt': new_task.createdAt,
                'updatedAt': new_task.updatedAt,
                }
            if new_task.id == 1:
                data_list = []
            else:
                with open(filename, encoding='utf-8') as file:
                    data_list = json.load(file)
        # add data to data_list
            data_list.append(data)
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data_list, f, indent=4, default=str)
            print('Task added successfully (ID: ' + str(new_task.id) + ')')
        
            count += 1
            with open(add_filename, 'w') as f:
                f.write(str(count))
        else:
            print('The description is empty')
    else:
        print('Nonsense words')

def update_task(message):
    index = message.find('"')
    description = message[index:]
    if description.startswith('"') and description.endswith('"'):
        description = description[1:-1]
        if description != '':
            try:
                task_id = int(message[16: index - 1])
                with open(filename) as f:
                    data_list = json.load(f)
                for data in data_list:
                    for key, value in data.items():
                        if value == task_id:
                            data['description'] = description
                            data['updatedAt'] = datetime.now()
                            with open(filename, 'w', encoding='utf-8') as f:
                                json.dump(data_list, f, indent=4, default=str)
                            print('Task updated successfully (ID: ' + 
                                str(task_id) + ')')
                            return
                print('Task ' + str(task_id) + ' is not found')
            except ValueError:
                print('Nonsense words')
        else:
            print('The description is empty')
    else:
        print('Nonsense words')
    
def delete_task(message):
    try:
        id_number = int(message[16:])
        with open(filename) as f:
            data_list = json.load(f)
        for data in data_list:
            for key, value in data.items():
                if value == id_number:
                    del data_list[id_number - 1]
                    with open(filename, 'w', encoding='utf-8') as f:
                        json.dump(data_list, f, indent=4, default=str)
                    print('Task deleted successfully (ID: ' + 
                        str(id_number) + ')')
                    return
        print('Task ' + str(id_number) + ' is not found')
    except ValueError:
        print('Nonsense words')

def mark_in_progress(message):
    try:
        id_number = int(message[26:])
        with open(filename) as f:
            data_list = json.load(f)
        for data in data_list:
            for key, value in data.items():
                if value == id_number:
                    data['status'] = 'in-progress'
                    data['updatedAt'] = datetime.now()
                    with open(filename, 'w', encoding='utf-8') as f:
                        json.dump(data_list, f, indent=4, default=str)
                    print('Task marked as in-progress successfully (ID: ' + 
                        str(id_number) + ')')
                    return
        print('Task ' + str(id_number) + ' is not found')
    except ValueError:
        print('Nonsense words')

def mark_done(message):
    try:
        id_number = int(message[19:])
        with open(filename) as f:
            data_list = json.load(f)
        for data in data_list:
            for key, value in data.items():
                if value == id_number:
                    data['status'] = 'done'
                    data['updatedAt'] = datetime.now()
                    with open(filename, 'w', encoding='utf-8') as f:
                        json.dump(data_list, f, indent=4, default=str)
                    print('Task marked as done successfully (ID: ' + 
                        str(id_number) + ')')
                    return
        print('Task ' + str(id_number) + ' is not found')
    except ValueError:
        print('Nonsense words')

def list_all():
    with open(filename) as f:
        data_list = json.load(f) 
    if data_list:
        for data in data_list:
            print(data['description'])
    else:
        print('There is no task')

def list_done():
    data_list_done = []
    with open(filename) as f:
        data_list = json.load(f)
    for data in data_list:
        if data['status'] == 'done':
            data_list_done.append(data)
    if data_list_done:
        for data_done in data_list_done:
            print(data_done['description'])
    else:
        print('There is no task marked as done')
 
def list_todo():
    data_list_todo = []
    with open(filename) as f:
        data_list = json.load(f)
    for data in data_list:
        if data['status'] == 'to do':
            data_list_todo.append(data)
    if data_list_todo:
        for data_todo in data_list_todo:
            print(data_todo['description'])
    else:
        print('There is no task marked as todo')
    
def list_in_progress():
    data_list_in_progress = []
    with open(filename) as f:
        data_list = json.load(f)
    for data in data_list:
        if data['status'] == 'in-progress':
            data_list_in_progress.append(data)
    if data_list_in_progress:
        for data_in_progress in data_list_in_progress:
            print(data_in_progress['description'])
    else:
        print('There is no task marked as in-progress')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
