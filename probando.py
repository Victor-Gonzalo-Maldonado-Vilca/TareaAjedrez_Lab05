from chessPictures import *
from interpreter import draw
x = square.under(rock.negative()).up(square.negative().under(rock)).horizontalRepeat(4)
draw(x)