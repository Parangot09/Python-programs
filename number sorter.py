def sort(nums):

    for i in range(5):
        minpos = i
        for j in range(i,6):
            if num[j] < nums[minpos]:
                minpos = j


        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp



num = [4,5,6,8,1,7,9]
sort(num)

print(num)
