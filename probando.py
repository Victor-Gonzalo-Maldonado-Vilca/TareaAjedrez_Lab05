from chessPictures import *
from interpreter import draw
x = square.under(rock.negative()).horizontalMirror().verticalMirror().up(king).verticalRepeat(7)
draw(x)