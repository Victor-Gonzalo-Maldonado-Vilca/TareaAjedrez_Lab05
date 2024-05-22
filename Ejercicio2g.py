from interpreter import draw
from chessPictures import *
fila = square.join(square.negative()).horizontalRepeat(4)
fichas = rock.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rock)
peones = pawn.horizontalRepeat(8)
fichasBlancas = fila.negative().under(fichas).up(fila.under(peones)) 
fichasNegras = fila.negative().under(peones.negative()).up(fila.under(fichas.negative()))
tablero = fichasBlancas.up(fila.negative().up(fila).verticalRepeat(2)).up(fichasNegras)
draw(fila.under(tablero))