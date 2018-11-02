import math

def find_next_square(sq):
    root = math.sqrt(sq)
    if root - math.floor(root)==0:
        x = root+1
        square = x*x
        return int(square)
    else:
        return -1