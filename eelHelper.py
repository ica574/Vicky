import eel

def letConn():
    count = 0

    while True:
        eel.sleep(1)
        count = count + 1

        if(count > 10):
            print("Break this batch!")
            break
        continue