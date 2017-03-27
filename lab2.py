import math

def add(a, b):
  return a ^ b

def mul(a, b):
  a0 = a % 2
  a1 = (a % 4) >> 1
  a2 = (a % 8) >> 2

  b0 = b % 2
  b1 = (b % 4) >> 1
  b2 = (b % 8) >> 2

  c0 = (a0 & b0) ^ (a1 & b2) ^ (a2 & b1) ^ (a2 & b2)
  c1 = (a0 & b1) ^ (a1 & b0) ^ (a2 & b2)
  c2 = (a0 & b2) ^ (a1 & b1) ^ (a2 & b0) ^ (a1 & b2) ^ (a2 & b1) ^ (a2 & b2)

  return (c2 << 2) ^ (c1 << 1) ^ c0

def inv(a):
  if a == 0:
    return 0
  if a == 1:
    return 1
  m = [1, 2, 4, 5, 7, 3, 6, 1]
  return m[7 - m.index(a)]

def matmul(A, a):
  a0 = a % 2
  a1 = (a % 4) >> 1
  a2 = (a % 8) >> 2

  c0 = (A[0] & a0) ^ (A[1] & a1) ^ (A[2] & a2)
  c1 = (A[3] & a0) ^ (A[4] & a1) ^ (A[5] & a2)
  c2 = (A[6] & a0) ^ (A[7] & a1) ^ (A[8] & a2)

  return (c2 << 2) ^ (c1 << 1) ^ c0

def subbytes(a):
  A = [1, 0, 0, 1, 1, 1, 1, 0, 1]
  a1 = inv(a)
  b = matmul(A, a1)
  return add(b, 3)

def subbytes_full(a):
  A = br_word(a)
  B = [None] * len(A)
  for i in range(0, len(B)):
    B[i] = subbytes(A[i])
  return (B[0] << 9) ^ (B[1] << 6) ^ (B[2] << 3) ^ B[3]

def cirshi(a, n, lim=3):
  m = 1 << lim
  a = a << n
  if a >= m:
    a = (a % m) ^ (a >> lim)
  return a

def powX(i):
  m = [1, 2, 4, 5, 7, 3, 6]
  if i >= len(m):
    i = i % len(m)
  return m[i]

def br_word(a):
  A = [None] * 4
  A[0] = (a % (1 << 12)) >> 9
  A[1] = (a % (1 << 9)) >> 6
  A[2] = (a % (1 << 6)) >> 3
  A[3] = (a % (1 << 3))
  return A


def keyshed(k, it=10):
  W = br_word(k)
  W = W + ([None] * (it * 4))
  K = [k]

  for i in range(0, it):
    j = i + 1
    jj = 4 * j
    T = cirshi(W[jj - 1], 2)

    T = subbytes(T)
    T = T ^ powX(j)
    W[jj] = W[jj - 4] ^ T
    W[jj + 1] = W[jj - 3] ^ W[jj]
    W[jj + 2] = W[jj - 2] ^ W[jj + 1]
    W[jj + 3] = W[jj - 1] ^ W[jj + 2]

    newkey = (W[jj] << 9) ^ (W[jj + 1] << 6) ^ (W[jj + 2] << 3) ^ W[jj + 3]
    K.append(newkey)
  return K

def transpose(A):
  dd = len(A)
  d = int(math.sqrt(dd))
  B = [None] * dd
  for i in range(0, d):
    for j in range(0, d):
      B[i * d + j] = A[j * d + i]
  return B

# A: a00 a01 a10 a11
def mixcol(a):
  M = [2, 3, 1, 2]
  A = br_word(a)
  A1 = transpose(A)
  b00 = mul(M[0], A[0]) ^ mul(M[1], A[2])
  b01 = mul(M[0], A[1]) ^ mul(M[1], A[3])
  b10 = mul(M[2], A[0]) ^ mul(M[3], A[2])
  b11 = mul(M[2], A[1]) ^ mul(M[3], A[3])
  B = transpose([b00, b01, b10, b11])
  return (B[0] << 9) ^ (B[1] << 6) ^ (B[2] << 3) ^ B[3]

def shirow(a):
  A = br_word(a)
  B = [A[0], A[1], A[3], A[2]]
  return (B[0] << 9) ^ (B[1] << 6) ^ (B[2] << 3) ^ B[3]

def enc(m, k):
  K = keyshed(k)
  a = m
  a = a ^ K[0]
  for i in range (1, 10):
    a = subbytes_full(a)
    a = shirow(a)
    a = mixcol(a)
    a = a ^ K[i]
  a = subbytes_full(a)
  a = shirow(a)
  a = a ^ K[10]
  return a

k = 0b101010010111
# print mul(5, 3)
# print inv(7)
# for i in range(0, 8):
#   print subbytes(i)
# KK = keyshed(k)
# for k in KK:
#   print bin(k)
# print bin(mixcol(0b100100111101))
m = 0b010010101100
print bin(enc(m, k))
