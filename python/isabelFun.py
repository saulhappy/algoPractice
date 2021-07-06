import time

def isabelFun():
    counter = 1
    while counter < 100001:
        print(f"{counter}: PAC-MAN")
        counter += 1
        time.sleep(0.01)

isabelFun()