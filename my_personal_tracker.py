from datetime import datetime

dict_task = {}

#Creating the class of adding tasks cus people are obvs gonna make more then one
class AddingTask():
	def __init__(self, task_name, priority, progression, deadline):
		self.task_name = task_name
		self.priority = priority
		self.progression = progression
		self.deadline = deadline
		self.temp_list = []
		self.temp_list.append(self.priority)
		self.temp_list.append(self.progression)
		self.temp_list.append(self.deadline)
		dict_task[self.task_name] = self.temp_list #Allows acceses to all the details based of the key

#Validating + Getting The Task Name
def get_task_name(prompt):
	while True:
		task_name = input(prompt).strip().capitalize()
		if task_name == "":
			print("Error: Please ensure dont leave it empty")
			print("\n")
			continue
		else:
			return task_name

#Validating + Getting The Priority
def get_priotity():
	while True:
		try:
			priority = int(input("Enter the priority of the set task between 1-5 (1 - being most important, and 5 being list important): ").strip())
			if priority not in [1, 2, 3, 4, 5]: #If its not these numers then Error since it has to be between 1-5
				print("Error: Ensure that the number added is between 1 - 5" )
				print("\n")
				continue
			else: 
				return priority
		except ValueError:
			print("Error: Ensure you added a number and that you havent left it empty. \n")

#Validating + Getting The Deadline
def get_dead_line():
	while True:
		try:
			deadline = input("Enter the deadline in the format of DD/MM/YYYY: ").strip()
			deadline = datetime.strptime(deadline,"%d/%m/%Y") #Validates by turning it into a DateTime Object
 #Formats it so that the hours mins and seconds are removed
			if deadline.date() <= datetime.now().date(): #Ensure the date is above current date
				print("Error: Ensure you're date is in the future not the past. ")
				print("\n")
				continue
			deadline = datetime.strftime(deadline,"%d/%m/%Y") #Formats it so that the hours mins and seconds are removed, turns date time object into a str
			return deadline
		except ValueError:
			print("Error: Ensure you dont leave it blank and enter numbers. Furthermore it shoudld be in the format of (DD/MM/YYYY). \n") # Type and Prescence Check.

#Validating + Getting The Progression
def get_progression():
	while True:
		progression = input("Enter progression as these options completed, not completed, in progress: ").lower()
		if progression not in ["completed", "not completed", "in progress"]:
			print("Error: Ensure its the 3 choices, completed, not completed, in progress.")
			print("\n")
			continue
		else:
			return progression

#Valdiating, type and precensce check the choices
def valid_choice(prompt):
	while True:
		try:
			var_choice = int(input(prompt).strip()) #Used strip in most code to remove trailing spaces.
			if var_choice <= 0:
				print("Error: Ensure the number is a postive number above 0")
				continue
			else:
				return var_choice
		except ValueError:
			print("Error: Ensure you have enter a number and that you havent left it blank/empty. \n")
			continue

#Adding The Tasks
def add_task():
	print("--- Number Of Tasks You Want To Add: ") 
	num_task = valid_choice("Enter the number of task: ")
	print("\n")
	#Calling the functions for the number of times a task needs to be added and appending them to a dictionary.
	for i in range(num_task):
		print(f"###  THE NUMBER OF TASKS: {i+1} ###")
		print("--- Task Name ---")
		task_name = get_task_name("Enter the name of the task you want to add: ")
		print("\n")
		print("--- Task Priority ---")
		priority = get_priotity()
		print("\n")
		print("--- Task Progression ---")
		progress = get_progression()
		print("\n")
		print("--- Task DeadLine ---")
		deadline = get_dead_line()
		print("\n")
		AddingTask(task_name, priority, progress, deadline)
		print("\n")

 
#Getting The Tasks and Viewing Them.
def get_dict():
	print("Demo View")
	print("---------------------")
	print("Task Detail in 'Task Name':")
	print("- Priority number")
	print("- Progression")
	print("- Deadline")
	print("---------------------")
	print("\n\n")
	print("The Real Tasks: ")
	sorted_dict = dict(sorted(dict_task.items(), key=lambda item: item[1]))
	for key, value in sorted_dict.items():
				if isinstance(value, list): #If the value is a list type then the condition is active.
					print("---------------------")
					print(f"Task Details In {key}:")
					for item in value:
						print(f"- {item}")
					print("---------------------")
					print("\n")

#Changing Progression
def change_progression():
	task_name = get_task_name("Enter the name of the task you want to change the progression of: ")
	if task_name in dict_task:
		for key, value in dict_task.items():
			if key == task_name:
				for item in value:
					del value[1] #Delete old progression
					new_progression =  get_progression() #Get new one and insert it back
					value.insert(1, new_progression)
					break
	else:
		print(f"Error: The '{task_name}' is not in the Data Base. Ensure you spelled it correct ")

#Change Priority
def change_priortiy():
	task_name = get_task_name("Enter the name of the task you want to change the priority of: ")
	if task_name in dict_task:
		for key, value in dict_task.items():
			if key == task_name:
				for item in value:
					del value[0] #Delte old priority
					new_priority =  get_priotity() #Get new priority and insert it into the old one
					value.insert(0, new_priority)
					break
	else:
		print(f"Error: The '{task_name}' is not in the Data Base. Ensure you spelled it correct ")

#Deleting Task
def delete_key():
	task_name = get_task_name("Enter the name of the task you want to delete: ")
	if task_name in dict_task:
		del dict_task[task_name] #Compelted remove the key
		print(f"Task named: {task_name}, has been delted")
	else:
		print(f"Error: The '{task_name}' is not in the Data Base. Ensure you spelled it correct ")

#Main Menu
def main():
	while True:
		print("### Smart To-Do List Main Menu ###")
		print("1. Add Task")
		print("2. View Task")
		print("3. Change Progression")
		print("4. Change Priority")
		print("5. Delete Task")
		print("6. Exit Program")
		print("\n")
		print("--- Choice ---")
		choice = valid_choice("Enter the number from 1 - 6: ")
		print("\n")
		if choice == 1:
			add_task()
		elif choice == 2:
			get_dict()
		elif choice == 3:
			change_progression()
		elif choice == 4:
			change_priortiy()
		elif choice == 5:
			delete_key()
		elif choice == 6:
			print("--- Exiting Program ---")
			print("Goodbye, Comeback soon.")
			break
		else:
			print("Error: Choice out of range, ensure its between 1 - 6")




#Calling Main
if __name__ == "__main__":
	main()
