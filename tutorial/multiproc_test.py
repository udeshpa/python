import time
import concurrent.futures
import multiprocessing

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleep {seconds} second(s) ')
    time.sleep(seconds)
    return f'Done sleeping in {seconds} second(s)'


p1 = multiprocessing.Process(target=do_something, args=[1.5])
p2 = multiprocessing.Process(target=do_something, args=[1.5])

p1.start()
p2.start()

p1.join()
p2.join()

processes = []
for _ in range(10):
    p = multiprocessing.Process(target=do_something, args=[1.5])
    p.start()
    processes.append(p)

for p in processes:
    p.join()


with concurrent.futures.ProcessPoolExecutor() as executor: #automatically join the processes
    f1 = executor.submit(do_something, 1.5)
    print(f1.result())
    seconds = [5, 4, 3, 2, 1]
    futures = [executor.submit(do_something, sec) for sec in seconds]
    for f in concurrent.futures.as_completed(futures):
        print(f.result())

    results = executor.map(do_something, seconds)
    for r in results:
        print(r)


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds')
