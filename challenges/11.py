import random
import time

q = int(input("Output only one number or output until stopped? (1 or 2): "))

if q == 1:
    print(random.randint(1, 100))
elif q == 2:    
    while True:
        print(random.randint(1, 100))
        time.sleep(0.1)
