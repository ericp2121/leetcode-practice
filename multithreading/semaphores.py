import threading
import time

# allow only 2 chores to run at once
semaphore = threading.Semaphore(2)

def walk_dog(name, last):
    with semaphore:
        print(f'{name} {last} waiting to walk the dog...')
        time.sleep(8)
        print('walking the dog,', name, last)

def take_out_trash():
    with semaphore:
        print('waiting to take out trash...')
        time.sleep(2)
        print('taking out trash')

def get_mail():
    with semaphore:
        print('waiting to get the mail...')
        time.sleep(4)
        print('getting the mail')

chore1 = threading.Thread(target=walk_dog, args=('scooby', 'doo'))
chore2 = threading.Thread(target=take_out_trash)
chore3 = threading.Thread(target=get_mail)

chore1.start()
chore2.start()
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print('all chores finished!')
