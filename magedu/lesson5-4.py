import random
import  time
def data_source():
    while True:
        yield random.randint(0,100)
        time.sleep(0.1)

ds = data_source()

import datetime
def top_k1(k,time = 3):
    start = datetime.datetime.now()
    lst = []
    while True:
        e = next(ds)
        for i,v in enumerate(lst):
            if e < v:
                lst.insert(i,e)
                break
        else:
            lst.append(e)
        current = datetime.datetime.now()
        if (current - start).total_seconds() >= time:
            start = current
            lst.sort()
            ret = []
            for _ in range(k):
                ret.append(lst.pop())
                yield ret
g2 = top_k1(10)
for _ in range(10):
    print(next(g2))
