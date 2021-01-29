def last2(str):
  result = ""
  count = 0
  last2 = str[len(str)-2:]

  for i in range(len(str) - 1):
    result = result + str[i]
    if len(result) == 2:
      if result == last2:
        count += 1
        result = result[1]
      
      else:
        result = result[1]
        
  return count


print(last2('xxxx'))

