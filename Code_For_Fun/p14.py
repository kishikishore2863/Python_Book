#14. Define unique_list(nums) that returns a list with duplicates removed (preserving order).
def unique_list(nums):
    seen = []
    for n in nums:
        if n not in seen:
            seen.append(n)
    return seen

print(unique_list([1,2,2,3,1,4]))

