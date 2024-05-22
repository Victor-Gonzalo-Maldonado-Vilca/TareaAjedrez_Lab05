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
    if(len(p.img) != len(self.img)):
      return Picture(p.img)
    for value1,value2 in zip(self.img,p.img):
      cadena = ""
      for i in range(len(value1)):
        if(value2[i] == ' '):
          cadena += value1[i]
        else:
          cadena += value2[i]
      sobre.append(cadena)
    return Picture(sobre)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    repeath = []
    for value in self.img:
      cadena = ""
      for i in range(n):
        cadena += value
      repeath.append(cadena)
    return Picture(repeath)

  def verticalRepeat(self, n):
    repeatv = []
    for i in range(n):
      for value in self.img:
        repeatv.append(value)
    return Picture(repeatv)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    rotar = []
    for i in range (len(self.img[0])):
      for value in self.img:
        rotar.append(value[i])
    return Picture(rotar)

