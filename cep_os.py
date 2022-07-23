import threading
import time
import random


isTobacco = False
isMatch = False
isPaper = False


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
        while (True):
            item2 = random.randint(0, 2)
            if (item1 != item2):
                break

    itemList = [item1, item2]
    return itemList


def itemsOnTable():
    global mutex
    mutex.acquire()
    generatedNumbersList = generateRandomItems()
    tableItemsList = []
    for i in generatedNumbersList:
        print("Items on table:", ingredientsList[i])
        tableItemsList.append(ingredientsList[i])
    mutex.release()
    return (tableItemsList)


def smokerTobacco():
    haveIngredient = "tobacco"
    # print("I have ", end="")
    return (haveIngredient)


def smokerPaper():
    haveIngredient = "paper"
    # print("I have ", end="")
    return (haveIngredient)


def smokerMatch():
    haveIngredient = "match"
    # print("I have ", end="")
    return (haveIngredient)


def conditionCheck():

    global isTobacco, isMatch, isPaper

    varItemsOnTable = itemsOnTable()
    print(smokerMatch(),
          smokerTobacco(),
          smokerPaper())

    if smokerTobacco() not in varItemsOnTable:
        print("I don't have match for Tobacco")
        isTobacco = True
        return (isTobacco)

        # print(itemsOnTable())

    if smokerPaper() not in varItemsOnTable:
        print("I don't have match for Paper")
        isPaper = True
        return (isPaper)

        # print(itemsOnTable())

    if smokerMatch() not in varItemsOnTable:
        print("I don't have match for Matches")
        isMatch = True
        return (isMatch)

        # print(itemsOnTable())


def threads():
    t1 = thread_one()
    t2 = thread_two()
    t3 = thread_three()

    t1.start()
    t2.start()
    t3.start()

    return ("")


def executionMutex(ingredientBoolean):

    global isPaper, isTobacco, isMatch
    global mutex
    mutex.acquire()

    print(isTobacco, isPaper, isMatch)
    if isTobacco == True:
        print("Process Tobacco will run")
        # isTobacco = False

    if isPaper == True:
        print("Process Paper will run")

    if isMatch == True:
        print("Process Match will run")

    mutex.acquire()
    if ingredientBoolean == True:
        print("I have the ingredient")
        mutex.release()
        return (True)
    else:
        print("I don't have the ingredient")
        mutex.release()
        return (True)

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
    # b = itemsOnTable()
    # print(b)
    # smoker1 = smokerTobacco()
    # smoker2 = smokerPaper()
    # smoker3 = smokerMatch()
    # print(smoker1, smoker2, smoker3)


a = executionMutex(conditionCheck())
print(a)
