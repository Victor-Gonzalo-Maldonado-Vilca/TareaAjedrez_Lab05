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
    longitud = len(self.img)
    horizontal = [self.img[longitud - i - 1] for i in range (longitud)]
    return Picture(horizontal)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    negativo = [''.join(self._invColor(pixel) for pixel in value) for value in self.img]
    return Picture(negativo)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    alado = [value1 + value2 for value1,value2 in zip(self.img,p.img)]
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
    repeatv = [value for i in range(n) for value in self.img]
    return Picture(repeatv)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    rotar = [''.join(self.img[c][i] for c in range(len(self.img) - 1, -1, -1)) for i in range(len(self.img[0]))]
    return  Picture(rotar)

