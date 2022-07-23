import threading
import time
import random

mutex = threading.Lock()
ingredientsList = ["tobacco", "paper", "matches"]


class thread_one(threading.Thread):
    def run(self):
        global mutex
        print("Time of first thread", time.strftime(
            "%H:%M:%S", time.localtime()))
        print("The first thread is now sleeping")
        time.sleep(random.randint(1, 3))
        print("First thread is finished")
        mutex.release()
        print("Time of release of first thread",
              time.strftime("%H:%M:%S", time.localtime()))


class thread_two(threading.Thread):
    def run(self):
        global mutex
        print("Time of second thread", time.strftime(
            "%H:%M:%S", time.localtime()))
        print("The second thread is now sleeping")
        time.sleep(random.randint(1, 3))
        mutex.acquire()
        print("Second thread is finished")
        mutex.release()
        print("Time of release of second thread",
              time.strftime("%H:%M:%S", time.localtime()))


class thread_three(threading.Thread):
    def run(self):
        global mutex
        print("Time of third thread", time.strftime(
            "%H:%M:%S", time.localtime()))
        time.sleep(random.randint(1, 3))
        mutex.acquire()
        print("Third thread is finished")
        mutex.release()


def generateRandomItems():
    item1 = random.randint(0, 2)
    item2 = random.randint(0, 2)
    if (item1 == item2):
        item2 = item2 + 1
    itemList = [item1, item2]
    return itemList


def itemsOnTable():
    global mutex
    mutex.acquire()
    generatedNumbersList = generateRandomItems()
    for i in generatedNumbersList:
        print("Items on table:", ingredientsList[i])
    mutex.release()
    return ""


# mutex.acquire()
# t1 = thread_one()
# t2 = thread_two()
# t3 = thread_three()
# print(threading.active_count())
# t1.start()
# t2.start()
# t3.start()
# print("\n", threading.active_count())

# separately generating items on table
# a = generateRandomItems()
# print(a)


b = itemsOnTable()
print(b)
