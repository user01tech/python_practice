n = int(input("Enter number of elements: "))

nums = []

for i in range(n):
    num = int(input("Enter element: "))
    nums.append(num)

target = int(input("Enter target: "))

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print("Indices are:", [i, j])
            break