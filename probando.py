from chessPictures import *
from interpreter import draw
x = square.under(knight).horizontalRepeat(4).verticalMirror().horizontalMirror()
draw(x)