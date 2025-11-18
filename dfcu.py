from typing import Callable
import time
import datetime
import math
import random

from huublogsetup import CliLogger
#logger = CliLogger("python.crfiles.dfcu")
#logger.set_formatter(logger.long_formatter)
#logger.handler.setLevel("DEBUG")

logger = CliLogger("python.crfiles.dfcu")

def set_logger(l):
    global logger
    logger = l

def random_list_selector(anylist: list[str])->Callable[[],str]:
    def selector()->str:
        return random.choice(anylist)
    return selector

def unique_int(digits:int)->int:
    return random.randint(10**(digits-1),(10**digits)-1)

def unique_int_growing(time_digits:int = 0, random_digits:int = 0)->str:
    if time_digits < 0:
        #logger.error(f"unique_id_growing({time_digits=:d}): minimum number of digits is 0.")
        raise ValueError(f"unique_id_growing({time_digits=:d}): minimum number of digits is 0.")
    if random_digits < 0:
        #logger.error(f"unique_id_growing({random_digits=:d}): minimum number of digits is 0.")
        raise ValueError(f"unique_id_growing({random_digits=:d}): minimum number of digits is 0.")
    if time_digits < 2:
        logger.warn(f"unique_id_growing({time_digits=:d}): Are you sure you want {time_digits:d} time digit(s)?")
    if random_digits < 2:
        logger.warn(f"unique_id_growing({random_digits=:d}): Are you sure you want {random_digits:d} random digit(s)?")

    # note: if we would use straight decimal for time digits,
    # we run a chance of having one or moere zero initial digits.
    # But we need a number not starting with zeros to make sure that
    # even after conversion to a decimal int, we dont lose digits.
    # solution: we make the time a base 9 number, with symbols 1-9 instead of the normal 0-8.
    # (fidling with the base 10 number has the chance of loosing continuous increasing time value
    t = int(time.time()*10)
    if time_digits == 0:
        tstring = "" 
    else:
        tlog9 = math.log(t, 9)
        if tlog9 < time_digits:
            logger.error(f"unique_id_growing({time_digits=:d}): time = {t}: not enough digits in current time.")
        # get the necessary (lowest significant) base 9 digits [1-9] from t
        tstring = ""
        i = 0
        while t > 0 and i < time_digits:
            tstring += chr((t%9)+49)
            t //= 9
            i += 1
        tstring = tstring[::-1]

    if random_digits == 0:
        rstring = "" 
    else:
        rvalue = random.randint(10**(random_digits-1),(10**random_digits)-1)
        rstring = f"{rvalue}"

    r = tstring + rstring

    logger.debug(f"unique_id_growing( {time_digits=}, {random_digits=}): time()*10={t} {tstring=} {rstring=} returning {r=}.")
    return r

def debug_unique_int_growing():
    try:
        x = unique_int_growing(-1, 5)
    except ValueError as e:
        logger.error(e)
    try:
        x = unique_int_growing(5, -1)
    except ValueError as e:
        logger.error(e)
    x = unique_int_growing(100, 5)
    x = unique_int_growing(0,0)
    x = unique_int_growing(1,1)
    x = unique_int_growing(2,2)
    x = unique_int_growing(3,3)
    x = unique_int_growing(10,10)
    x = unique_int_growing(10,20)

def date_list(from_date:datetime.date|None = None, to_date:datetime.date|None = None)->list[datetime.date]:
    if not ( isinstance(from_date, datetime.date) and isinstance(to_date, datetime.date) ):
        raise ValueError("date_list(): from_date and to_date must be of type datetime.date.")
    ndays:datetime.timedelta = to_date - from_date
    if ndays.days < 1:
        raise ValueError("date_list(): to_date must be larger than from_date.")
    oneday = datetime.timedelta(days = 1)
    i = ndays.days + 1
    l = []
    d = from_date
    while i > 0:
        l.append(d)
        i -= 1
        d += oneday
    return l

def debug_date_list():
    oneday = datetime.timedelta(days = 1)
    d1 = datetime.date(2025,1,1)
    d2 = datetime.date(2025,2,1)
    dd = d2-d1
    if dd.days != 31:
        logger.error(f"{dd.days=} January has 31 days!")
    else:
        logger.debug(f"January has 31 days.")
    l = date_list(d1, d2 - oneday)
    logger.debug(f"{len(l)=} Should be 31")
    logger.debug(f"{l[0]=} {l[30]=}")


