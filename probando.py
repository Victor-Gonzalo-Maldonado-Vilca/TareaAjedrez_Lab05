from chessPictures import *
from interpreter import draw
x = square.under(rock.negative()).join(square.negative().under(king)).horizontalRepeat(4)
draw(x)