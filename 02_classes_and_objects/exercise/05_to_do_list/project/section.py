from project.task import Task


class Section:

    def __init__(self, name: str) -> None:
        self.name = name
        self.tasks: list = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        tsk: Task = next((t for t in self.tasks if t.name == task_name), None)
        if tsk:
            tsk.completed = True
            return f"Completed task {tsk.name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        count = 0
        for task in self.tasks:
            if task.completed:
                count += 1

        return f"Cleared {count} tasks."

    def view_section(self):
        details = '\n'.join(task.details() for task in self.tasks)
        return f"Section {self.name}:\n{details}"
