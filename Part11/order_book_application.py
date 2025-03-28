# Write your solution here
# If you use the classes made in the previous exercise, copy them here

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

  def add_order(self,task_desc:str,programmer:str,workload:int)->None:
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
  
  def finished_orders(self) -> list:
    return [task for task in self.tasks if task.is_finished()]
  
  def unfinished_orders(self) -> list:
    return [task for task in self.tasks if not(task.is_finished())]

  def status_of_programmer(self, programmer: str) -> tuple:

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

class OrderBookUI():
  def __init__(self):
    self.orderbook = OrderBook()

  def help(self) -> None:
    print("commands: ")
    print("0 exit")
    print("1 add order")
    print("2 list finished tasks")
    print("3 list unfinished tasks")
    print("4 mark task as finished")
    print("5 programmers")
    print("6 status of programmer")

  def add_order(self) -> None:

    try:
      description = input("description: ")
      programmer_and_workload = input("programmer and  workload estimate: ")
      programmer,workload = programmer_and_workload.split(" ")
      self.orderbook.add_order(description,programmer,int(workload))
      print("added!")
    except:
      print("erroneous input")
  
  def finished_orders(self) -> None :
    tasks = self.orderbook.finished_orders()

    if len(tasks) == 0:
      print("no finished tasks")
      return
    
    for task in tasks:
      print(task)

  def unfinished_orders(self) -> None :
    tasks = self.orderbook.unfinished_orders()

    if len(tasks) == 0:
      print("no finished tasks")
      return
    
    for task in tasks:
      print(task)

  def mark_finished(self) -> None:
    try:
      task_id = int(input("id: "))
      self.orderbook.mark_finished(task_id)
      print("marked as finished")
    except:
      print("erroneous input")

  def programmers(self) -> None:
    get_programmers = self.orderbook.programmers()
    for programmer in get_programmers:
      print(programmer)

  def status_of_programmer(self) -> None:
    try:
      programmer = input("programmer: ")
      get_status = self.orderbook.status_of_programmer(programmer)
      
      print(f"tasks: finished {get_status[0]} not finished {get_status[1]}, hours: done {get_status[2]} scheduled {get_status[3]}")
    except:
      print("erroneous input")
  
  def execute(self) -> None :
    self.help()
    while True:
      print()
      command = int(input("command: "))

      if command == 0:
        break

      if command == 1:
        self.add_order()

      if command == 2:
        self.finished_orders()
 
      if command == 3:
        self.unfinished_orders()

      if command == 4:
        self.mark_finished()

      if command == 5:
        self.programmers()

      if command == 6:
        self.status_of_programmer()

orderbookui = OrderBookUI()
orderbookui.execute()