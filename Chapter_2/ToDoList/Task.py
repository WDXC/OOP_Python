import datetime


taskid = 0

class Item:
    """
    Item need have these property:
        1. taskid
        2. TaskName
        3. DeadLine
        4. Progress status
    """
    def __init__(self, taskname, deadline):
        global taskid
        taskid += 1
        self._taskid = taskid
        self._taskname = taskname
        self._dealine = deadline
        self._status = "unstarted"


class Task:
    def __init__(self):
        self.items = []

    def AddNewEntry(self, taskname, dealine):
        now = datetime.datetime.now()
        time = now + datetime.timedelta(minutes=int(dealine))
        self.items.append(Item(taskname, time))

    def ModifyDeadline(self, taskid, deadline):
        for item in self.items:
            if item._taskid == taskid:
                item._dealine = deadline
                break

    def ModifyStatus(self, taskid, status):
        for item in self.items:
            if item._taskid == taskid:
                item._status = status
                break

    def ModifyTaskName(self, taskid, taskname):
        for item in self.items:
            if item._taskid == taskid:
                item._taskname = taskname
                break

    def DelExistTaskById(self, taskid):
        self.items = [item for item in self.items if item._taskid != taskid ]

    def DelExistTaskByName(self, taskname):
        self.items = [item for item in self.items if item._taskname != taskname ]