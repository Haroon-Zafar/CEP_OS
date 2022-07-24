
import threading
import time
import random
# import thread

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
            print("The Tobacco thread has now locked the process")

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
            print("The Paper thread has now locked the process")

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
            print("The Match thread has now locked the process")

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

    # threads()

    # print(itemsOnTable())


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

    print("Total Number of Running Threads: ", threading.active_count())

    t1_tobacco.join()
    t2_paper.join()
    t3_match.join()
    print("bye")

    return ("")


def executionMutex(ingredientBoolean):

    global isPaper, isTobacco, isMatch
    global mutex
    # mutex.acquire()

    threads()

    # mutex.release()

    return (True)


def commonMethod():
    global mutex
    global t1_tobacco, t2_paper, t3_match

    # mutex.acquire()
    print(isTobacco, isPaper, isMatch)

    if isTobacco == True:
        print("Process Tobacco will run")
        # t2_paper.join()
        # t3_match.join()

        # cigaretteMaking()
        # isTobacco = False

    if isPaper == True:
        print("Process Paper will run")
        # cigaretteMaking()
        # t1_tobacco.join()
        # t3_match.join()

    if isMatch == True:
        print("Process Match will run")
        # cigaretteMaking()
        # t1_tobacco.join()
        # t2_paper.join()

    # mutex.release()


def cigaretteMaking():

    print("I am making a cigarette")
    print("Cigarette has been Made")
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


# def Agent():
#     a = executionMutex(conditionCheck())
#     print(a)


# Agent()


# mutex.acquire()
# threads()
# t1 = thread_one()
# t2 = thread_two()
# t3 = thread_three()
varItemsOnTable = conditionCheck()
a = executionMutex(varItemsOnTable)
# commonMethod()
# # print(a)


# t1.start()
# t2.start()
# t3.start()

# print(threading.active_count())
