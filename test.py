import math

print("Finding HCF and LCM\n")

x = int(input("Enter 1st no:"))
y = int(input("Enter 2nd no:"))


# def my_hcf(x, y):
#     while (y):
#         x, y = y, x % y
#     return x
#
#
# def my_lcm(x, y):
#     return (x * y) / my_hcf(x, y)
#
#
# print("\nHCF is: ", my_hcf(x, y))
# print("LCM is: ", my_lcm(x, y))

def my_hcf(x, y):
    return math.gcd(x, y)


def my_lcm(x, y):
    return (x * y) / my_hcf(x, y)


hcf = my_hcf(6, 3)
lcm = my_lcm(6, 3)
print(hcf, lcm)
