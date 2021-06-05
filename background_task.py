

import time
def background_task(n, index):
    """ Function that returns len(n) and simulates a delay """
    delay = 5
    print(f"Simulating a {delay} second delay")
    print(f"task number {index}")
    time.sleep(delay)
    print(len(n))
    return len(n)