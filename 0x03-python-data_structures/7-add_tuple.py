#!/ust/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    first_elem = 0
    second_elem = 0

    if tuple_b == ():
        first_elem = tuple_a[0]
        second_elem = tuple_a[1]
    elif len(tuple_b) < 2:
        if tuple_b[0] == None:
            first_elem = tuple_a[0]
            second_elem = tuple_a[1] + tuple_b[1]
        else:
            first_elem = tuple_a[0] + tuple_b[0]
            second_elem = tuple_a[1] 
    else:
        first_elem = tuple_a[0] + tuple_b[0]
        second_elem = tuple_a[1] + tuple_b[1]
    
    return((first_elem, second_elem)) 
