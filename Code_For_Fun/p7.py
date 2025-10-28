

#7.  Write a function calc_sum_avg(numbers) that takes a list of integers and returns both the sum and average.
def calc_sum_avg(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg

nums = [1, 2, 3, 4, 5]
print(calc_sum_avg(nums))

