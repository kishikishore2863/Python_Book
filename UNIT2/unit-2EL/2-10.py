#A math helper class uses a static method to check for prime numbers.
# You must run it on a list of numbers.

class MathHelper:
    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

nums = [1, 2, 3, 4, 17, 20, 23]

for n in nums:
    print(n, "→", MathHelper.is_prime(n))