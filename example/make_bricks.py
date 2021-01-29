def make_bricks(small, big, goal):
  if goal - (small + big * 5) == 0:
    return True
  elif goal - small == 0 or goal - big * 5 == 0:
    return True
  for i in range(small):
    for j in range(big):
      if goal == i + j * 5:
        return Ture
  else:
    return False
