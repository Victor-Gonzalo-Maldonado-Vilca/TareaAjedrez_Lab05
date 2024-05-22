from chessPictures import *
from interpreter import draw
x = knight.up(rock).verticalMirror().horizontalMirror()
draw(x)