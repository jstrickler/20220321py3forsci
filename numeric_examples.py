#  int float
i1 = 100
i2 = 29302385203985203958209358029830958203958029385029385292671212582235342342

print(i1 + i2)
print(0b11000011, 0xDEADBEEF, 0o377)

f1 = 123.456
f2 = .456
f3 = 80.0
f4 = 1.9383e17

a = 23
b = 8
print(a + b, a - b)
print(a * b, a / b, a // b, a // -b)
#  // floored divison -- round to nearest whole number
print(a ** b, a % b)

b += 2   #   b = b + 2
b *= 5
b /= 10
print("b: {}".format(b))

b += 1  # adds 1 to b

#  NOT AVAILABLE: b++  etc

a = "123"
b = 456
print(a + str(b))
print(int(a) + b)
print(float(a) + b)










