from PIL import Image, ImageOps
import os
from .combinations import * # noqa

def flip(seq):
    seq = seq.replace('l','x')
    seq = seq.replace('j','l')
    seq = seq.replace('x','j')
    seq = seq.replace('s','x')
    seq = seq.replace('z','s')
    seq = seq.replace('x','z')
    return seq

def solve(p,reverse=False):
    """
    p: a 4-letter string, the first is the hold piece, and the next three are the three pieces you have next.
    reverse: False if the hook is on the right, True if the hook is on the left.
    
    Returns images of all possible perfect clear sequences. If reverse is True, the color of some of the blocks 
    might be wrong.
    """
    flag = 0
    
    possible = set()
    for a, b, c in orders:
        possible.add(p[a]+p[b]+p[c])


    for seq in possible:
        for c in combos:
            if ((flip(seq) in c) if reverse else (seq in c)):
                flag = 1
                print(seq)
                image = Image.open(f'pictures/{c[-1]}')
                image = image.resize((394,214))
                if reverse:
                    image = ImageOps.mirror(image)
                image.show()
                return

    if flag == 0:
        print('YOU ARE FUCKED')
