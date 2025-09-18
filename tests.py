from calculator import add, subtract, multiply, divide, power, square_root

print("2 + 3", add(2, 3), "Expected: 5")
print("10 - 6", subtract(10, 6), "Expected: 4")
print("4 * 5", multiply(4, 5), "Expected: 20")
print("100 / 4", divide(100, 4), "Expected: 25")
print("3 / 0", divide(3, 0), "Expected: Cannot divide by 0.")
print("2 ** 3", power(2, 3), "Expected: 8")
print("49", square_root(49), "Expected: 7")
print("-4", square_root(-4), "Expected: Cannot take the square root of a negative number.")