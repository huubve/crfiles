#import typer
from typing import Callable, NamedTuple
import time
import math
import random
import datetime

from huublogsetup import CliLogger
logger = CliLogger("python.crfiles.main")

import dfcu # Data File Creation Utilities
dfcu.set_logger(logger)

def get_netnrs(filename:str) -> list[str]:
    l:list[str] = []
    with open(filename) as netnrsfile:
        for line in netnrsfile:
            # file has two tab-separeted columns: net-nr, major-city-name
            nr, _ = line.split("\t")
            l.append(nr)
    return l

def get_familynames(filename:str) -> list[str]:
    l:list[str] = []
    with open(filename) as famnamesfile:
        for line in famnamesfile:
            # file has two tab-separeted columns: famyliname, nr-of-occurrences
            name, _ = line.split("\t")
            l.append(name)
    return l

class observationOrder(NamedTuple):
    id:int = -1
    nr:int = -1
    name:str = ""
    start:datetime.date = datetime.date(year=1960, month=3, day=2)
    end:datetime.date =  datetime.date(year=1960, month=3, day=2)
    def __str__(self):
        return f"{self.id}\t{self.nr}\t{self.name}\t{self.start}\t{self.end}"

def observation_order(start_days:list[datetime.date], min_days, max_days, somenet, somename )-> observationOrder:
    if random.randint(0,1):
        netnr = "316" # mobile phones
    else:
        netnr = somenet()
    subdigits = 10 - len(netnr)
    subnr = dfcu.unique_int(subdigits)
    r = observationOrder(
        dfcu.unique_int(20),
        f"{netnr}{subnr}",
        somename(),
        (s := random.choice(start_days)),
        s + datetime.timedelta(days = random.randrange(min_days, max_days))
    )
    return r



def main()->int:
    #logger.set_formatter(logger.short_formatter)
    #logger.handler.setLevel("ERROR")
    logger.set_formatter(logger.long_formatter)
    logger.handler.setLevel("DEBUG")
    # dfcu.debug_unique_int_growing()
    # dfcu.debug_date_list()
    netnumbers:list[str]                = get_netnrs("../infiles/netnummers.txt")
    familynames:list[str]               = get_familynames("../infiles/famnamen.txt")
    some_netnumber:Callable[[],str]     = dfcu.random_list_selector(netnumbers)
    some_familyname:Callable[[],str]    = dfcu.random_list_selector(familynames)
    #logger.debug(f"{some_netnumber()=}")
    #logger.debug(f"{some_familyname()=}")
    startdates = dfcu.date_list(datetime.date(2024,12,17), datetime.date(2025,11,10))
    i = 10
    while ( i := i-1 ) > 0:
        oo = observation_order(startdates, 14, 40, some_netnumber, some_familyname)
        print(str(oo))

    return 0


if __name__ == "__main__":
    main()
