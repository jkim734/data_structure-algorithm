from enum import Enum
from fixed_queue import FixedQueue

Menu = Enum('Menu', ['Enqueue', 'Dequeue', 'Peek', 'Search', 'Dump', 'Exit'])

def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end = '')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

q = FixedQueue(64)

while True:
    print(f'The Number of current Data: {len(q)}/{q.capacity}')
    menu = select_menu()
    
    if menu == Menu.Enqueue:
        x = int(input('type Data to Enqueue: '))
        try:
            q.enque(x)
        except FixedQueue.Full:
            print("Queue is Full")
            
    elif menu == Menu.Dequeue:
        try:
            q.deque()
        except FixedQueue.Empty:
            print("Queue is empty")
    
    elif menu == Menu.Peek:
        try:
            x = q.peek()
            print(f'peek data is {x}')
        except FixedQueue.Empty:
            print("Queue is empty")
            
    elif menu == Menu.Search:
        try:
            x = int(input('type data to search: '))
            if x in q:
                print(f'{q.count(x)} of them are in, first index is {q.find(x)}')
            else:
                print('cannot find')
            print(f'peek data is {x}')
        except FixedQueue.Empty:
            print("Queue is empty")
        
    elif menu == Menu.Dump:
        q.dump()
    else:
        break