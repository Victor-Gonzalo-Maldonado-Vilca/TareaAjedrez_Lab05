from chessPictures import *
from interpreter import draw
x = square.under(knight.negative()).verticalMirror().horizontalMirror().join(rock)
draw(x)