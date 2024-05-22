from chessPictures import *
from interpreter import draw
x = knight.up(rock).verticalMirror().horizontalMirror().negative().up(rock)
draw(x)