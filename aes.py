import bit
import poly

M = [
  0b11110001,
  0b11100011,
  0b11000111,
  0b10001111,
  0b00011111,
  0b00111110,
  0b01111100,
  0b11111000
]

# assume a is strictly 8-bit
def subbytes(a):
  a1 = poly.inverse(a, 0x11b)
  r = 0
  for i in range(0, 8):
    r = r + (bit.odd1(M[i] & a1) << i)
  r = r ^ 0b01100011
  return r

# table lookup version, should be faster
# def subbytes2(a):
