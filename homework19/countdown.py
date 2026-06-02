import time
for i in range(5, 0, -1):
    print(f"{i:3d}", end = "\r")
    time.sleep(1)