import time
import random

heads= int(0)
tails=int(0)
a = int(random.randint(1,2))

if a<=1:
    print("Tossing.... "
          time.sleep(2)
          " Heads  ( 1 )")
    heads=heads+1
    
else:
    print("Tossing.... ",time.sleep(2),"Tails   ( 2 )")
    tails=tails+1


a = int(random.randint(1,2))

if a<=1:
    print("Tossing.... Heads  ( 1 )")
    heads=heads+1
    
else:
    print("Tossing.... Tails   ( 2 )")
    tails=tails+1
    
    





if heads>=tails :
    print("Winner: Heads")
else:
    print("Winner: Tails")
    
