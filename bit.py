# count nb of 1's in a (bin)
def nb1(a):
  s = 0
  while a > 0:
    s = s + (a % 2)
    a = a >> 1
  return s

# test if nb of 1's is odd
def odd1(a):
  return nb1(a) % 2

# count length of bit sequence
def bit_len(a):
  l = 0
  while a > 0:
    a = a >> 1
    l = l + 1
  return l
