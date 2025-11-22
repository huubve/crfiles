import dfcu
import time
import polars

def records():
    for i in range(10000000):
        yield({"i":i,"s":chr(48+i%26),"u":dfcu.unique_int_growing(6,6)})

df = polars.from_dicts(records())
print(df)
