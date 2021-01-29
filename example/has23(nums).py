def has23(nums):
  for num in range(len(nums)):
    if nums[num] == 2 or nums[num] == 3:
      return True
    else:
      return False

print(has23([4,3]))