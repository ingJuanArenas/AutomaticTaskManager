from datetime import datetime
from typing import Callable


def log_Action(func:Callable):
    def wrapper(*args, **kargs):
        with LogContext("tareas.txt") as log:
            log.write(f"[{datetime.now()}] se he ejecutado: [{func.__name__}]\n")
        return func(*args,**kargs)
    return wrapper
    


class LogContext:
    def __init__(self, filename:str):
        self.filename= filename
    def __enter__(self):
        self.file= open(self.filename, "a", encoding="utf-8")
        return self.file
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

