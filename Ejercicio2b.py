from interpreter import draw
from chessPictures import *
fila = knight.join(knight.negative())
draw(fila.verticalMirror().up(fila))
