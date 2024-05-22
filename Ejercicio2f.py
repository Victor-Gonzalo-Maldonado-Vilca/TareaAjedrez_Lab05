from interpreter import draw
from chessPictures import *
fila = square.join(square.negative()).horizontalRepeat(4)
draw(fila.negative().up(fila).verticalRepeat(2))