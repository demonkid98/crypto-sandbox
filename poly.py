import bit

def div(a, b):
  n = a
  aq = 0
  while True:
    q = bit.bit_len(n) - bit.bit_len(b)
    if q < 0:
      break
    aq = aq + (1 << q)
    n = n ^ (b << q)
  return aq, n

def mul(a, b):
  s = 0
  i = 0
  while b > 0:
    if b % 2 == 1:
      s = s ^ (a << i)
    b = b >> 1
    i = i + 1
  return s

def eec(a, b):
  l = [a, b]
  u = [1, 0]
  v = [0, 1]

  r = b
  while True:
    q, r = div(l[-2], l[-1])
    if r == 0:
      break
    l.append(r)
    u.append(u[-2] ^ mul(q, u[-1]))
    v.append(v[-2] ^ mul(q, v[-1]))
  return l[-1], u[-1], v[-1]

def inverse(a, b):
  return eec(a, b)[1]

