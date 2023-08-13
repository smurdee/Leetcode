nums = input()
target = int(input())
nums = nums[1:-2]
nums = nums.split(',')

for i in range(len(nums)):
    j = i + 1
    while (j < len(nums) - 1):
        if ((int(nums[i]) + int(nums[j])) == target):
            print([i, j])
            break
            break
        j += 1