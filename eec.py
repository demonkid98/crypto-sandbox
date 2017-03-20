def eec(a, b):
  l = [a, b]
  u = [1, 0]
  v = [0, 1]

  r = b
  while True:
    q = l[-2] / l[-1]
    r = l[-2] % l[-1]
    if r == 0:
      break
    l.append(r)
    u.append(u[-2] - q * u[-1])
    v.append(v[-2] - q * v[-1])

  return l[-1], u[-1], v[-1]

def inverse(a, b):
  return eec(a, b)[1]
