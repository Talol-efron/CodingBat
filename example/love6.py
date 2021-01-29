def love6(a, b):
  x = 0
  if a == 6 or b == 6:
    return True
  else:
    if a + b == 6:
      return True
    if a - b == 6:
      return True
    if b - a == 6:
      return True
    else:
      return False


print(love6(1,5))
