# set of integers list ==> iterate over each element ==> and set them as powers for 2,3,5

# def numberdivisibleby(number):
#     factorslist = []
#     for i in range(1,number+1):
#         if number % i ==0:
#             factorslist.append(i)

    
    
#     return factorslist
# def powersList(list1):
#     powersArray = []
#     pow2 = 0
#     pow3 = 0
#     pow5 = 0
#     result = ""
#     for item in list1:
#        factorsList =  numberdivisibleby(item)
#        print(f"{item} -  {factorsList}")

    
# numberList = list(map(int, input("Enter numbers:: ").split(' ')))

# powersList(numberList)

def prime_factorization(n):
    factors = {}
    i = 2

    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i] = factors.get(i, 0) + 1

    if n > 1:
        factors[n] = factors.get(n, 0) + 1

    return factors

def convert_to_prime_powers(num):
    prime_factors = prime_factorization(num)
    result = []

    for factor, exponent in prime_factors.items():
        result.append(f"{factor} ^ {exponent}")

    return " * ".join(result)

# Example usage:
number = 10
result = convert_to_prime_powers(number)
print(f"{number} = {result}")


