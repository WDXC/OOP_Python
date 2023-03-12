import sys
from Task import Item, Task

class Menu:
    def __init__(self):
        self.Task = Task()
        self.choices = {
            '1': self.ShowTask,
            '2': self.AddTask,
            '3': self.ModifyTaskName,
            '4': self.ModifyTaskDeadline,
            '5': self.ModifyTaskStatus,
            '6': self.DeleteTaskById,
            '7': self.DeleteTaskByName,
            '8': self.Quit,
        }

    def Display(self):
        print(
            """
            To-Do List
            1. Show All Task
            2. Add a new Task
            3. Modify Task Name
            4. Modify Task Deadline
            5. Modify Task Status
            6. Delete Task by Task id
            7. Delete Task by Task name
            8. Quit
            """
        )

    def run(self):
        while True:
            self.Display()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def ShowTask(self, task=None):
        if not task:
            task = self.Task.items
        for item in task:
            print("{0}: {1}\t{2}\t{3}".format(
                item._taskid, item._taskname,
                item._dealine, item._status
            ))

    def AddTask(self):
        taskname = input("Enter a TaskName: ")
        deadline = input("Enter a Deadline: ")
        self.Task.AddNewEntry(taskname, deadline)

    def ModifyTaskName(self):
        taskid = input("Enter Task id: ")
        taskname = input("Enter a TaskName: ")
        self.Task.ModifyTaskName(taskid, taskname)

    def ModifyTaskDeadline(self):
        taskid = input("Enter Task id: ")
        deadline = input("Enter a DeadLine: ")
        self.Task.ModifyDeadline(taskid, deadline)

    def ModifyTaskStatus(self):
        taskid = input("Enter Task id: ")
        deadline = input("Enter a DeadLine: ")
        self.Task.ModifyStatus(taskid, deadline)

    def DeleteTaskById(self):
        taskid = input("Enter Task id: ")
        self.Task.DelExistTaskById(taskid)

    def DeleteTaskByName(self):
        taskname = input("Enter a TaskName: ")
        self.Task.DelExistTaskByName(taskname)

    def Quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()