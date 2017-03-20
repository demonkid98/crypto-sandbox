import bit
import eec
import poly
import aes

# print eec.eec(8, 3)
# print eec.inverse(8, 5)

# print hex(poly.mul(0x9, 0x3))
# print hex(poly.mul(0x9, 0x2))
# print hex(poly.mul(0x9, 0x7))
# print hex(poly.mul(0x9, 0x5))
# print hex(poly.mul(0x9, 0x4))

# print hex(poly.inverse(0xf6, 0x11b))
# print hex(poly.inverse(0xcb, 0x11b))

# print bit.nb1(0b111)
# print bit.nb1(0b11)
# print bit.nb1(0b1001)
# print bit.nb1(0b110001)

print hex(aes.subbytes(0xf6))
print hex(aes.subbytes(0x1d))
print hex(aes.subbytes(0x42))
print hex(aes.subbytes(0x6e))
