def array_front9(nums):
  if len(nums) > 4:
    for num in range(4):
      if nums[num] == 9:
        return True 
    else:
        return False
  else:
    for num in range(len(nums)):
      if nums[num] == 9:
        return True
    else:
        return False
      
    


print(array_front9([1, 2, 9]))
