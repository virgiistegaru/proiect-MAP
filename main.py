from datetime import datetime, date

def sortare_taskuri_dupa_prioritate():
    with open('taskuri.txt', 'r') as f:
        taskuri = f.readlines()
    taskuri.sort(key=lambda x: int(x.strip().split(',')[2]), reverse=True)
    with open('taskuri.txt', 'w') as f:
        f.writelines(taskuri)

def afisare_taskuri():
    with open('taskuri.txt', 'r') as f:
        sortare_taskuri_dupa_prioritate()
        taskuri = f.readlines()
        for idx, task in enumerate(taskuri):
            task_info = task.strip().split(',')
            print(f"{idx + 1}. Task: {task_info[0]}, Descriere: {task_info[1]}, Prioritate: {task_info[2]}, Data limita: {task_info[3]}, Status: {task_info[4]}")
        if not taskuri:
            print('Nu exista taskuri in lista.')

def adaugare_task():
    while(1):
        task = input('Introduceti noul task: ')
        if task.strip() == '' or ',' in task or '.' in task:
            print('Numele task-ului nu poate fi gol.')
            continue
        break
    descriere = input('Introduceti descrierea task-ului: ')
    prioritate = input('Introduceti prioritatea task-ului (1-5): ')
    if prioritate=="":
        prioritate='3'
        print('Prioritate setata implicit la 3.')
    while True:
        ddl = input('Introduceti data limita (format ZZ-LL-AAAA): ')
        try:
            task_ddl = datetime.strptime(ddl, '%d-%m-%Y').date()
            if task_ddl < date.today():
                print('Data limita nu poate fi in trecut. Incercati din nou.')
                continue
            break
        except ValueError:
            print('Format data invalida. Incercati din nou.')
    status='Necompletat'
    with open('taskuri.txt', 'a') as f:
        f.write(f"{task},{descriere},{prioritate},{task_ddl},{status}\n")

def stergere_task():
    print('Introduceti numele task-ului de sters:')
    nume_task=input()
    with open('taskuri.txt', 'r') as f:
        taskuri = f.readlines()
        for idx, task in enumerate(taskuri):
            task_info = task.strip().split(',')
            if task_info[0] == nume_task:
                del taskuri[idx]
                print(f'Task-ul "{task_info[0]}" a fost eliminat.')
                break
        if not any(task_info[0] == nume_task for task in taskuri):
            print(f'Task-ul "{nume_task}" nu a fost gasit.')  
    with open('taskuri.txt', 'w') as f:
        f.writelines(taskuri)

def modificare_status():
    print('Introduceti numele task-ului pentru modificare status:')
    nume_task=input()
    with open('taskuri.txt', 'r') as f:
        taskuri = f.readlines()
        for idx, task in enumerate(taskuri):
            task_info = task.strip().split(',')
            if task_info[0] == nume_task:
                if task_info[4] == 'Completat':
                    task_info[4] = 'Necompletat'
                else:
                    task_info[4] = 'Completat'
                taskuri[idx] = ','.join(task_info) + '\n'
                print(f'Statusul task-ului "{task_info[0]}" a fost modificat la "{task_info[4]}".')
                break
        if not any(task_info[0] == nume_task for task in taskuri):
            print(f'Task-ul "{nume_task}" nu a fost gasit.')  
    with open('taskuri.txt', 'w') as f:
        f.writelines(taskuri)
    
    print('Status modificat cu succes.')
    

def stergere_total():
    with open('taskuri.txt', 'w') as f:
        f.write('')



while(1):
    print('Alegeti o optiune:')
    print('1. Afisare lista taskuri')
    print('2. Adaugare task nou')
    print('3. Stergere task')
    print('4. Modificare status task (complet/incomplet)')
    print('5. Stergere toate taskurile')
    print('6. Iesire')
    optiune = input('Introduceti optiunea (1-6): ')
    if optiune == '1':
        afisare_taskuri()
    elif optiune == '2':
        adaugare_task()
    elif optiune=='3':
        stergere_task()
    elif optiune=='4':
        modificare_status()
    elif optiune == '5':   
        stergere_total()
    elif optiune == '6':
        print('Iesire din aplicatie.')
        break
    else:
        print('Optiune invalida. Incercati din nou.')
    
    