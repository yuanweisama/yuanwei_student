import sympy

# 将输入值转化成浮点数
p = float(input('p'))
K = float(input('k'))

# 假设一个未知数x
x = sympy.Symbol('x')

# 设置方程内容
a = x / (1 - x)
b = 2 * p / (2 + x)
eq = sympy.Eq(a * (b ** 0.5), K)
# 将获得的参数储存到resp
resp = sympy.solve(eq)

print(resp)
