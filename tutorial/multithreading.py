import threading
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleep {seconds} second(s) ')
    time.sleep(seconds)
    return f'Done sleeping in {seconds} second(s)'


t1 = threading.Thread(target=do_something, args=[1.5])
t2 = threading.Thread(target=do_something, args=[1.5])

t1.start()
t2.start()

t1.join()
t2.join()

threads = []
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for t in threads:
    t.join()


import concurrent.futures

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    futures = [executor.submit(do_something, sec) for sec in secs]
    for f in concurrent.futures.as_completed(futures):
        print(f.result())

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    futures = executor.map(do_something, secs)
    for f in futures:
        print(f)


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds')

