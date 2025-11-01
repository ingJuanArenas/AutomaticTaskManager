
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Task:
    name: str
    deadline: datetime
    completed: bool = field(default=False)

    def days_left(self) -> int:
        return (self.deadline - datetime.now()).days
    def __str__(self) -> str:
        return f"Task: {self.name}, Deadline: {self.deadline}, Status: {'Completed' if self.completed else 'Pending'}"


