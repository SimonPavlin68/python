import sympy as sym

x, y = sym.symbols('x y')
# Make two plots with different colors.
p1 = sym.plot(x**2, (x, -1, 1), show=False, line_color='b')
p2 = sym.plot(x**3, (x, -1, 1), show=False, line_color='r')
# Make the second one a part of the first one.
p1.extend(p2)
# Display the modified plot object.
p1.show()

