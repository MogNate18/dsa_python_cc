print(f"This is a List")
marks = [2,8,9,7,10]
print(marks[2])
print(f"**********************************************************************")

print(f"This is a Tuple")
person = ("Nathan", 18, "Chacha", 3456, "Strathmore University")
print(person[3])

print(f"***********************************************************************")
print(f"This is a dictionary")
house = {"Name":"The Chacha's", "Age":10, "Road":"Mwanaichi road", "Court":"Zawadi"}
house ={"Age":9}
print(house["Age"])

print(f"***********************************************************************")
print(f"This is a set")
cars = {"BMW","Mercedes","Audi","Porsche"}
cars.add("Cardillac")
cars.add("Range Rover")
cars.add("Lexus")
cars.add("Toyota")
cars.remove("Audi")
cars.remove("Porsche")
cars.remove("Mercedes")
print(cars)

print(f"***********************************************************************")
print(f"This is a stack")
from collections import deque

# Initialize the stack
history_stack = deque()

# 1. PUSH: Adding items to the stack
print("--- STACK: PUSHING ITEMS ---")
history_stack.append("Homepage.com")
history_stack.append("Dashboard.com")
history_stack.append("Settings.com")
print(f"Current Stack (Top is on the right): {list(history_stack)}\n")

# 2. POP: Removing items from the stack (Last-In, First-Out)
print("--- STACK: POPPING ITEMS (LIFO) ---")
popped_page1 = history_stack.pop()
print(f"Clicked 'Back' button. Removed: {popped_page1}")
print(f"Stack now: {list(history_stack)}\n")

popped_page2 = history_stack.pop()
print(f"Clicked 'Back' button again. Removed: {popped_page2}")
print(f"Stack now: {list(history_stack)}")

print(f"***********************************************************************")
print(f"This is a Queue")
from collections import deque

# Initialize the queue
print_queue = deque()

# 1. ENQUEUE: Adding items to the queue
print("--- QUEUE: ENQUEUEING ITEMS ---")
print_queue.append("Document_1.pdf")
print_queue.append("Photo_2.png")
print_queue.append("Report_3.docx")
print_queue.append("Invoice_4.xlsx")
print(f"Current Queue (Front is on the left): {list(print_queue)}\n")

# 2. DEQUEUE: Removing items from the queue (First-In, First-Out)
print("--- QUEUE: DEQUEUEING ITEMS (FIFO) ---")
served_job1 = print_queue.popleft()
print(f"Printed: {served_job1}")
print(f"Queue now: {list(print_queue)}\n")

served_job2 = print_queue.popleft()
print(f"Printed: {served_job2}")
print(f"Queue now: {list(print_queue)}\n")

served_job3 = print_queue.popleft()
print(f"Printed: {served_job3}")
print(f"Queue now: {list(print_queue)}")



