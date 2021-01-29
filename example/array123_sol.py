def array123(nums):
  # Note: iterate with length-2, so can use i+1 and i+2 in the loop
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False

print(array123([1, 1, 2, 1, 2, 2, 3]))


####[1,2,3]の並びがどこかにできればおk####
####自分が作ったのは、[1,2,3]が引数のどこかに揃ってなくてもあれば良いもの####