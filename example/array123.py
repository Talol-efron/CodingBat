def array123(nums):
  result = []
  array = [1,2,3]
  
  for num in range(len(nums)):
    if nums[num] == 1 or 2 or 3:
      if not 1 in result:
        result.append(nums[num])
      else:
        if not 2 in result and result == [1] and nums[num] == 2:
          result.append(nums[num])
        else:
          if not 3 in result and result == [1,2] and nums[num] == 3:
            result.append(nums[num])
    if array == result:
      return True
        
    
  else:
    return False
      

print(array123([1, 1, 2, 4, 1]))
