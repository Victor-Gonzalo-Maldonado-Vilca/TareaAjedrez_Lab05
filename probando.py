from chessPictures import *
from interpreter import draw
x = square.under(rock).up(king).rotate().verticalMirror()
draw(x)