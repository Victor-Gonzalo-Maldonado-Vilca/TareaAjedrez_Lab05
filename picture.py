from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
      vertical.append(value[::-1])
    return Picture(vertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    horizontal = []
    longitud = len(self.img)
    for i in range (longitud):
      horizontal.append(self.img[longitud - i - 1])
    return Picture(horizontal)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    negativo = []
    for value in self.img:
      valueNegative = ""
      for i in range(len(value)):
        valueNegative += self._invColor(value[i])
      negativo.append(valueNegative)
    return Picture(negativo)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    alado = []
    i = 0
    for value in self.img:
      alado.append(value)
    for value in p.img:
      alado[i] += value
      i += 1
    return Picture(alado)

  def up(self, p):
    encima = p.img + self.img
    return Picture(encima)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    sobre = []
    for value1,value2 in zip(self.img,p.img):
      cadena = ""
      for i in range(len(self.img)):
        if(value1[i] != ''):
          cadena += value2[i]
        else:
          cadena += value1[i]
      sobre.append(cadena)
    return Picture(cadena)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    return Picture(None)

  def verticalRepeat(self, n):
    return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

