from interpreter import draw
from chessPictures import *
fila = square.join(square.negative()).horizontalRepeat(4)
fichas = rock.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rock)
draw(fila.under(fichas))