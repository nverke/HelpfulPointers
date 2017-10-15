def fib(n,cache):
  if n <= 1:
    return n;
  elif cache[n] != 0:
    return cache[n];
  else:
    cache[n] = fib(n-1,cache) + fib(n-2,cache)
    return cache[n]

def answer():
    n = int(raw_input("Enter number"));
    cache = (n+1)*[0];
    return fib(n, cache)

print (answer())
