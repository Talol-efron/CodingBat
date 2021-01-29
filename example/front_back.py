####間違いはどこ？####


def front_back(str):
  n = len(str)
  front = str[0]
  midle = str[1:n-1]
  back = str[n-1]
  
  if 1 < n <= 2:
    return back + front
  elif n > 2:
    return back + midle + front
  else:
    return str

print(front_back("a"))
