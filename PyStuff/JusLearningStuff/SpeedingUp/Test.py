import time
import concurrent.futures

def running():
    ar = []
    for i in range(2, 50001):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            ar.append(i)
    return ar

# Using concurrent.futures.ThreadPoolExecutor
t1 = time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:
    try:
        results = executor.submit(running)
        ar = results.result()
        print("ThreadPool_ExecTime:", time.time() - t1)
        print("Result:", ar)
    except Exception as e:
        print("An error occurred:", e)


# Using concurrent.futures.ProcessPoolExecutor with more worker processes
t1 = time.time()
with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
    try:
        results = executor.submit(running)
        ar = results.result()
        print("ProcessPool_ExecTime:", time.time() - t1)
        print("Result:", ar)
    except Exception as e:
        print("An error occurred:", e)

t1 = time.time()
running()
t2 = time.time()
print("Normal_ExecTime:", t2 - t1)



'''import time
import multiprocessing

cores = multiprocessing.cpu_count()
print(cores)
pool = multiprocessing.Pool(cores)

ar = []

def running():
    for i in range(2, 1001):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            ar.append(i)

t1 = time.time()
pool.apply(running)
t2 = time.time()
print("Pool_ExecTime:", t2 - t1)


t1 = time.time()
running()
t2 = time.time()
print("Normal_ExecTime:", t2 - t1)

'''


'''
ar_ = nb.typed.List()
t1_ = time.time()

@nb.jit(nopython=True)
def running_jit():
    for i in range(2, 10001):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            ar_.append(i)

running_jit()

t2_ = time.time()
print("JIT_ExecTime:", t2_ - t1_)
'''

