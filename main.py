from datetime import datetime, date

from tabulate import tabulate

def sortare_taskuri_dupa_prioritate():
    with open('taskuri.txt', 'r') as f:
        taskuri = f.readlines()
    taskuri.sort(key=lambda x: int(x.strip().split(',')[2]), reverse=True)
    with open('taskuri.txt', 'w') as f:
        f.writelines(taskuri)

def afisare_taskuri():

    sortare_taskuri_dupa_prioritate()

    with open('taskuri.txt', 'r') as f:
        taskuri = f.readlines()

    if not taskuri:
        print('Nu exista taskuri in lista.')
        print('-----------------------------------')
        return

    tabel = []  

    for task in taskuri:
        task_info = task.strip().split(',')
        tabel.append([
            task_info[0],
            task_info[1],
            task_info[2],
            task_info[3],
            task_info[4]
        ])

    antet = ['Nume Task', 'Descriere', 'Prioritate', 'Data Limita', 'Status']

    print(tabulate(tabel, headers=antet, tablefmt='grid'))
    


def adaugare_task():
    print('-----------------------------------')
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
        print('Task adaugat cu succes.')
    print('-----------------------------------')

def stergere_task():
    print('-----------------------------------')
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
    print('-----------------------------------')

def modificare_status():
    print('-----------------------------------')
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
    print('-----------------------------------')
    

def stergere_total():
    print('-----------------------------------')
    with open('taskuri.txt', 'w') as f:
        f.write('')
    print('Toate taskurile au fost sterse.')
    print('-----------------------------------')

def editare_task():
    print('-----------------------------------')
    task=input('Introduceti numele task-ului de editat: ')
    camp=input('Introduceti campul de editat (nume, descriere, prioritate, data): ')
    update=input('Introduceti update-ul: ')
    with open('taskuri.txt', 'r') as f:
        taskuri = f.readlines()
        for idx, t in enumerate(taskuri):
            task_info = t.strip().split(',')
            if task_info[0] == task:
                if camp == 'nume':
                    task_info[0] = update
                elif camp == 'descriere':
                    task_info[1] = update
                elif camp == 'prioritate':
                    task_info[2] = update
                elif camp == 'data':
                    task_info[3] = update
                else:
                    print('Camp invalid.')
                    return
                taskuri[idx] = ','.join(task_info) + '\n'
                print(f'Task-ul "{task_info[0]}" a fost actualizat.')
                break
        if not any(task_info[0] == task for task in taskuri):
            print(f'Task-ul "{task}" nu a fost gasit.')
    with open('taskuri.txt', 'w') as f:
        f.writelines(taskuri)
    print('-----------------------------------')

def cautare_task():
    print('-----------------------------------')
    termen = input('Introduceti termenul de cautare (nume/descriere): ').lower()
    with open('taskuri.txt', 'r') as f:
        taskuri = f.readlines()
        gasit = False
        for task in taskuri:
            task_info = task.strip().split(',')
            if termen in task_info[0].lower() or termen in task_info[1].lower():
                print(f'Task: {task_info[0]}, Descriere: {task_info[1]}, Prioritate: {task_info[2]}, Data limita: {task_info[3]}, Status: {task_info[4]}')
                gasit = True
        if not gasit:
            print('Nu s-au gasit taskuri care sa corespunda criteriului de cautare.')
    print('-----------------------------------')

print('===================================')
print('Bine ati venit in aplicatia de gestionare a taskurilor!')
while(1):
    print('Alegeti o optiune:')
    print('1. Afisare lista taskuri')
    print('2. Adaugare task nou')
    print('3. Stergere task')
    print('4. Modificare status task (complet/incomplet)')
    print('5. Stergere toate taskurile')
    print('6. Editare task')
    print('7. Cautare task dupa nume/descriere')
    print('8. Iesire')
    print('-----------------------------------')
    
    optiune = input('Introduceti optiunea (1-8): ')
    if optiune == '1':
        print('Doriti filtrarea taskurilor? (Da/Nu)')
        filtrare = input().lower()
        if filtrare == 'da':
            print('Alegeti filtrul:')
            print('1. Doar taskuri necompletate')
            print('2. Doar taskuri completate')
            print('3. Taskuri cu prioritate mare (4-5)')
            print('4. Taskuri cu data limita apropiata (3 zile)')
            filtru = input('Introduceti optiunea (1-4): ')
            with open('taskuri.txt', 'r') as f:
                taskuri = f.readlines()
                filtrate = []
                for task in taskuri:
                    task_info = task.strip().split(',')
                    if filtru == '1' and task_info[4] == 'Necompletat':
                        filtrate.append(task)
                    elif filtru == '2' and task_info[4] == 'Completat':
                        filtrate.append(task)
                    elif filtru == '3' and int(task_info[2]) >= 4:
                        filtrate.append(task)
                    elif filtru == '4':
                        ddl = datetime.strptime(task_info[3], '%Y-%m-%d').date()
                        if 0 <= (ddl - date.today()).days <= 3:
                            filtrate.append(task)
                if filtrate:
                    print('-----------------------------------')
                    for idx, task in enumerate(filtrate):
                        task_info = task.strip().split(',')
                        print(f"{idx + 1}. Task: {task_info[0]}, Descriere: {task_info[1]}, Prioritate: {task_info[2]}, Data limita: {task_info[3]}, Status: {task_info[4]}")
                    print('-----------------------------------')
                else:
                    print('Nu exista taskuri care sa corespunda filtrului ales.')
        else:
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
        editare_task()
    elif optiune == '7':
        cautare_task()  
    elif optiune == '8':
        print('Iesire din aplicatie...')
        break
    else:
        print('Optiune invalida. Incercati din nou.')
    
    print('Statistici:')
    with open('taskuri.txt', 'r') as f:
        taskuri = f.readlines()
        total_taskuri = len(taskuri)
        taskuri_completate = sum(1 for task in taskuri if task.strip().split(',')[4] == 'Completat')
        rata_finalizare = (taskuri_completate / total_taskuri * 100) if total_taskuri > 0 else 0
        taskuri_depasite = sum(1 for task in taskuri if datetime.strptime(task.strip().split(',')[3], '%d-%m-%Y').date() < date.today() and task.strip().split(',')[4] == 'Necompletat')
        print(f'Total taskuri: {total_taskuri}, Rata finalizare: {rata_finalizare}%, Taskuri depasite: {taskuri_depasite}')
    print('*********************************')
    print('Notificari:')
    with open('taskuri.txt', 'r') as f:
        taskuri = f.readlines()
        notificari = False
        for task in taskuri:
            task_info = task.strip().split(',')
            ddl = datetime.strptime(task_info[3], '%d-%m-%Y').date()
            if (ddl - date.today()).days <= 1 and task_info[4] == 'Necompletat':
                print(f'Astazi este termenul limita pentru task-ul: "{task_info[0]}".')
                notificari = True
            if ddl < date.today() and task_info[4] == 'Necompletat':
                print(f'Termenul limita pentru task-ul: "{task_info[0]}" a fost depasit!')
                notificari = True
        if not notificari:
            print('Nu aveti notificari pentru astazi.')
    print('===================================') 
    
