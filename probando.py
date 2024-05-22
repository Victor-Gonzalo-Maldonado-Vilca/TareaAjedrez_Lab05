from chessPictures import *
from interpreter import draw
x = knight.join(rock.negative()).join(rock).join(knight).horizontalMirror()
draw(x)