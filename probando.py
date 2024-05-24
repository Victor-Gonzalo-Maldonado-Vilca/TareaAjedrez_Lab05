from chessPictures import *
from interpreter import draw
x = knight.horizontalMirror().negative().verticalMirror().horizontalMirror()
draw(x)