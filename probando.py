from chessPictures import *
from interpreter import draw
x = square.under(king.negative()).join(square.negative().under(queen))
draw(x)