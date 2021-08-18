from collections.abc import Iterable
import time 


import argparse

class TimeSt: 
    def __init__(self, description=""): 
        self.begin_time = None 
        self.description = description
    def __enter__(self): 
        self.begin_time = time.time()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb): 
        print(f"{self.description} time cost: {time.time() - self.begin_time}") 
  
def tqdm2(iter_ins):
    assert isinstance(iter_ins, Iterable)
    length = len(iter_ins)
    print(f"begin : {time.ctime()}")
    cnt = 0
    for i in iter_ins: 
        cnt += 1
        print(f"\r{length} -> {cnt} ", end="") 
        yield i
    print(f"\nend: {time.ctime()}")
    
# 
parser = argparse.ArgumentParser()
parser.add_argument('--qqq', type=str, default="ddd")

args = parser.parse_args()

print(args.qqq)

a = range(7)
with TimeSt():
    for i in tqdm2(a):
        time.sleep(1)