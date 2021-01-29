def first_last6(nums):
  if 6 == (nums[0] or nums[-1]):　 
    # 6 == nums[0] or 6 == nums[-1] にはならない
    return True
  else:
    return False

print(first_last6([1,2,6]))