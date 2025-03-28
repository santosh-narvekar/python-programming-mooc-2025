# Write your solution here:

class Task:

  id = 0
  
  def __init__(self,description:str,programmer:str,workload:int):
    self.description = description
    self.workload = workload
    self.programmer = programmer
    self.isFinished = False
    self.id = Task.id + 1
    Task.id += 1 

  def is_finished(self) -> bool:
    return self.isFinished
  
  def mark_finished(self) -> None:
    self.isFinished = True

  def __str__(self) -> str:
    return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {"FINISHED" if self.isFinished else "NOT FINISHED"}"

class OrderBook():
  def __init__(self):
     self.tasks = []

  def add_order(self,task_desc,programmer,workload)->None:
     self.tasks.append(Task(task_desc,programmer,workload))

  def all_orders(self) -> list:
     return self.tasks

  def programmers(self) -> list:
     return list(set([ task.programmer for task in self.tasks ]))
  
  def mark_finished(self,task_id:int) -> None:
    for task in self.tasks:
      if task.id == task_id:
        task.mark_finished()
        return 
   
    raise ValueError("id not present")
  
  def finished_orders(self):
    return [task for task in self.tasks if task.is_finished()]
  
  def unfinished_orders(self):
    return [task for task in self.tasks if not(task.is_finished())]

  def status_of_programmer(self, programmer: str):

    if programmer not in self.programmers():
      raise ValueError 
    
    finished_tasks = [task for task in self.tasks
    if task.programmer == programmer and task.is_finished()]
    unfinished_tasks = [task for task in self.tasks
    if task.programmer == programmer and not(task.is_finished())]
    
    no_of_finished_tasks = len(finished_tasks)
    no_of_unfinished_tasks = len(unfinished_tasks)

    finished_task_workload = sum([ task.workload for task in finished_tasks ])
    unfinished_task_workload = sum([ task.workload for task in unfinished_tasks ])

    return (no_of_finished_tasks,no_of_unfinished_tasks,finished_task_workload,unfinished_task_workload)
