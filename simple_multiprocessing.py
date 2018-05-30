#!/usr/bin/env python
# can be used as a timeout method in simulation
from multiprocessing import Process
import time

def single_process(num):
   cnt = 0
   while cnt<num:
      print(cnt)
      cnt += 1
      time.sleep(1)

if __name__ == "__main__":
   for i in range(5):
      p = Process(target = single_process(i))
      p.start()
      p.join(10)

      if p.is_alive():
         print("running test {}...".format(i))
         p.terminate()
         p.join()
   
