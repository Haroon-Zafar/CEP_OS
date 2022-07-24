import threading
import time
import random

isTobacco = False
isMatch = False
isPaper = False


ingredientsList = ["tobacco", "paper", "matches"]

mutex = threading.Lock()


class thread_tobacco(threading.Thread):
    def run(self):
        global mutex

        print()
        print("Tobacco Thread is waiting")

        mutex.acquire()
        if(isTobacco):
            print()
            print("The Tobacco thread has now locked the process")
            print("Inside Tobacco: ")
            cigaretteMaking()

            # timeToSleep = random.randint(1, 5)
            timeToSleep = 3
            time.sleep(timeToSleep)

            # time.sleep(random.randint(1, 5))

        mutex.release()

        print("Tobacco thread is finished")
        print()


class thread_paper(threading.Thread):
    def run(self):
        global mutex
        # timeToSleep = random.randint(1, 5)
        print()
        print("Paper Thread is waiting")
        mutex.acquire()

        if(isPaper):
            print()
            print("The Paper thread has now locked the process")
            print("Inside Paper: ")

            cigaretteMaking()

            timeToSleep = 3
            time.sleep(timeToSleep)

        mutex.release()
        print("Paper thread is finished")
        print()


class thread_match(threading.Thread):
    def run(self):
        global mutex
        # timeToSleep = random.randint(1, 5)
        print()
        print("Match Thread is waiting")

        mutex.acquire()
        if(isMatch):
            print()
            print("The Match thread has now locked the process")
            print("Inside Match:")
            cigaretteMaking()

            timeToSleep = 3
            time.sleep(timeToSleep)

        mutex.release()
        print("Match thread is finished")


t1_tobacco = thread_tobacco()
t2_paper = thread_paper()
t3_match = thread_match()


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
    # mutex.acquire()
    generatedNumbersList = generateRandomItems()
    tableItemsList = []
    for i in generatedNumbersList:
        print("Items on table:", ingredientsList[i])
        tableItemsList.append(ingredientsList[i])
    # mutex.release()
    print()
    print("Out of the Total Ingredients: ")
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
        print("\nTobacco is not on table so it's Process will be called to make the combination of cigarette")
        isTobacco = True

        return (isTobacco)

        # print(itemsOnTable())

    if smokerPaper() not in varItemsOnTable:
        print("\nPaper is not on table so it's Process will be called to make the combination of cigarette")
        isPaper = True

        return (isPaper)

        # print(itemsOnTable())

    if smokerMatch() not in varItemsOnTable:
        print("\nMatch is not on table so it's Process will be called to make the combination of cigarette")
        isMatch = True

        return (isMatch)


def threads():
    commonMethod()

    if(isTobacco):
        t1_tobacco.start()
        t2_paper.start()
        t3_match.start()

    if(isPaper):
        t2_paper.start()
        t1_tobacco.start()
        t3_match.start()

    if(isMatch):
        t3_match.start()
        t1_tobacco.start()
        t2_paper.start()

    print()
    # print("Total Number of Running Threads: ", threading.active_count())

    t1_tobacco.join()
    t2_paper.join()
    t3_match.join()
    print("End Of Iteration")

    return ("")


def executionMutex(ingredientBoolean):

    global isPaper, isTobacco, isMatch
    global mutex

    threads()

    return (True)


def commonMethod():
    global mutex
    global t1_tobacco, t2_paper, t3_match

    if isTobacco == True:
        print("Process Tobacco will run")

    if isPaper == True:
        print("Process Paper will run")

    if isMatch == True:
        print("Process Match will run")


def cigaretteMaking():

    print("I am making a cigarette")
    print("Cigarette has been Made\n")
    return (True)


varItemsOnTable = conditionCheck()
a = executionMutex(varItemsOnTable)
