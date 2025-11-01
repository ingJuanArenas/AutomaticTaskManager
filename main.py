
from datetime import datetime
from service.task_service import Task_service

from models.tarea import Task

service = Task_service()


while True:
   try:
       print(""" 
        ==== REGISTRADOR DE TAREAS ====
          1. Registrar tarea
          2. Mostrar tareas pendientes
          3. Marcar tarea como completada
          4. Mostrar tareas vencidas
          5. Mostrar todo
          0. salir

        """)
    
       option= int(input("Ingrese una opcion: "))

       match option:
            case 1: 
                name = input("Ingrese el nombre de la tarea: ")
                date= input("Ingrese la fecha limite de la tarea: (YYYY-MM-DD) ")
                deadline = datetime.strptime(date, "%Y-%m-%d")
                service.add_task(Task(name, deadline))
            case 2: 
                service.get_pendant_task()
            case 3:
                service.mark_as_completed()
            case 4: 
                service.get_late_tasks()
            case 5:
                tasks= service.get_tasks()
                for task in tasks: 
                    print(task)
            case 0:
                break
            case _:
                print("Opcion invalida..")

   except ValueError:
       print("ERROR: Ingrese un tipo de dato valido")
   except Exception as e:
       print(f"ERROR: {e}")