# you can also pass a list in assert 
def brand(brand_name):
    assert brand_name in ["louis philipe",
                         'addidas',
                         "rebook",
                         "fastrack",
                         "spark"], "brand name must be international not a local brand name"
    return f"ya you are like {brand_name} brand .it is so cool "

n=input("enter the brand name ")
brand(n)








# doctests example
def add(x,y):
    """add together x,y
    
    >>> add(4,3)
    7
    
    >>> add(8, "hi")
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    
    >>> add(1,None)
    1
    
    >>> add(1,2)
    True
    
    >>> add(True,True)
    """
    return x+y