import functions as f

prompt = '\nWhat do you want to do right now?'
prompt += '\nEnter "q" to exit. '

while True:
    message = input(prompt)
    
    if message == 'q':
        break
    
    if message.startswith('task-cli add '):
        f.add_task(message)
    
    elif message.startswith('task-cli update '):
        f.update_task(message)
        
    elif message.startswith('task-cli delete '):
        f.delete_task(message)
        
    elif message.startswith('task-cli mark-in-progress '):
        f.mark_in_progress(message)
        
    elif message.startswith('task-cli mark-done '):
        f.mark_done(message)
        
    elif message == 'task-cli list':
        f.list_all()
        
    elif message == 'task-cli list done':
        f.list_done()
        
    elif message == 'task-cli list todo':
        f.list_todo()
        
    elif message == 'task-cli list in-progress':
        f.list_in_progress()
    
    else:
        print('Nonsense words')
