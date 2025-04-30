import secrets
import time
import random

p_time = 0
while p_time < 1000:
    random_shit = random.randint(100, 1000)
    bruh = secrets.token_hex(random_shit)
    print(bruh)
    time.sleep(0.2)
    p_time += 1

print("Hacked Nasa")
