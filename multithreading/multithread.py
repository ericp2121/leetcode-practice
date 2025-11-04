# good for I/O tasks, multiprocessing for CPU tasks

import threading
import time 

def walk_dog(name, last):
    time.sleep(8)
    print('walking the dog, ', name, last)

def take_out_trash():
    time.sleep(2)
    print('taking out trash')

def get_mail():
    time.sleep(4)
    print('getting the mail')


# walk_dog()
# take_out_trash()
# get_mail()

chore1 = threading.Thread(target=walk_dog, args=('scooby', 'doo',))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()


chore1.join()
chore2.join()
chore3.join()
# ensure program does not continue beyond until here

print('all chores finished!')


# order by time of completion 