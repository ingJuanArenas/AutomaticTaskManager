from dataclasses import dataclass, field
from datetime import datetime
from typing import Generator, List

from logger.logger import log_Action
from models.tarea import Task


@dataclass
class Task_service:
    tasks: List[Task] = field(default_factory= list)


    @log_Action
    def get_tasks(self)-> Generator[Task, None, None]:
        yield from self.tasks

    @log_Action
    def get_pendant_task(self)-> None:
        pendant_tasks = list(filter(lambda t: not t.completed, self.tasks))
        if len(pendant_tasks) == 0: 
            print("No hay tareas pendientes...")
        else:
            for task in pendant_tasks:
                print(f"Tarea: {task.name} (Faltan: {(task.deadline- datetime.now()).days} días) ")
    
    @log_Action
    def get_late_tasks(self)-> None:
        late_tasks=list(filter(lambda t: t.deadline < datetime.now(), self.tasks))
        if len(late_tasks) == 0:
            print("No hay tareas vencidas...")
        else:
            for task in late_tasks:
                print(task)
            
    @log_Action
    def add_task(self, task: Task) -> None:
        self.tasks.append(task)
        print(f"Task '{task.name}' added successfully.")
    @log_Action
    def mark_as_completed(self)-> None:
        name = input("Ingrese el nombre de la tarea a marcar como completada: ")
        task = next((t for t in self.tasks if t.name == name), None)
        if task:
            task.completed = True
            print(f"Tarea '{task.name}' marcada como completada.")
        else:
            print("Tarea no encontrada.")
    