x = input("How many numbers you want?")

z = int(x)

l = list((1,2,"buckle my shoe"))

def fib(n):

  a = 0
  b = 1

  if n == 1:
    print(a)

  else:
    for i in range(2,n):
      c = a + b
      a = b
      b = c
      print(c)


print(l)


fib(z)