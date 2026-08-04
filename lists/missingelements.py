class Solution:
    def findmissingelements(self,nums:list[int]) -> list[int]:
        n = []
        smallest = min(nums)
        largest = max(nums)
        for i in range(smallest,largest+1):
            if i not in nums:
                n.append(i)
        return n 

nums = list(map(int,input("enter the numbers but please separate them with a space --> ").split()))
obj = Solution()
result = obj.findmissingelements(nums)
print(result)

         