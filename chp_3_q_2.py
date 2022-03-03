def do_twice(func):
    func()
    func()

def do_four(func):
    do_twice(func)
    do_twice(func)

def draw():
    print("+ - - - - ",end=" ")
    
def draws():
    print("!         ",end=" ")
    
def sample():
    do_twice(draw)
    print('+')

def sample1():
    do_twice(draws)
    print("!")

def row():
    sample()
    do_four(sample1)
    

def grid():
    do_twice(row)
    sample()
    

grid()