n = int(input("enter the length of the list --> "))
nums = []
for i in range(n):
    nums.append(int(input("enter element --> ")))

target = int(input("enter the target value --> "))
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])
            break
    else:
        continue
    break
else:
    print("No two sum solution found.")