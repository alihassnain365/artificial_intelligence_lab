"""
Exercise 1.1
Type each of the following expressions into python3. What value do each of the following Python
expressions evaluate to? Is that value an integer or a floating point?
a. 250
b. 28 % 5
c. 2.5e2
d. 3e5
e. 3 * 10**5
f. 20 + 35 * 2
Why is this different from (20 + 35) * 2?
g. 2 / 3 * 3
h. 2 // 3 * 3
Why is this different from 2 / 3 * 3?
i. 25 - 5 * 2 - 9
Is this different from ((25 - 5) * 2) - 9 and/or 25 - ((5 * 2) - 9)? Why?
"""

# Exercise 1.1

a = 250
b = 28 % 5
c = 2.5e2
d = 3e5
e = 3 * 10**5

f1 = 20 + 35 * 2
f2 = (20 + 35) * 2

g = 2 / 3 * 3
h = 2 // 3 * 3

i1 = 25 - 5 * 2 - 9
i2 = ((25 - 5) * 2) - 9
i3 = 25 - ((5 * 2) - 9)

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))

print(f1, type(f1))
print(f2, type(f2))

print(g, type(g))
print(h, type(h))

print(i1, type(i1))
print(i2, type(i2))
print(i3, type(i3))