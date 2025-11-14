#import typer



def get_netnrs(filename:str) -> list[str]:
    l = []
    with open(filename) as netnrsfile:
        for line in netnrsfile:
            nr, _ = line.split("\t")
            l.append(nr)
    return l

def get_famnames(filename:str) -> list[str]:
    l = []
    with open(filename) as famnamesfile:
        for line in famnamesfile:
            name, _ = line.split("\t")
            l.append(name)
    return l

def main():
    print("Hello from crfiles!")
    netnumbers = get_netnrs("../infiles/netnummers.txt")
    famnames = get_famnames("../infiles/famnamen.txt")


if __name__ == "__main__":
    main()
