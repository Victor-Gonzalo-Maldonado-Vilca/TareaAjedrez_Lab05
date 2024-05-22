from interpreter import draw
from chessPictures import *
fila = square.join(square.negative()).horizontalRepeat(4)
fichas = rock.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rock)
peones = pawn.horizontalRepeat(8)
fichasBlancas = fila.negative().under(fichas).up(fila.under(peones)) 
fichasNegras = fila.negative().under(peones.negative()).up(fila.under(fichas.negative()))
draw(fila.under(fichasNegras))