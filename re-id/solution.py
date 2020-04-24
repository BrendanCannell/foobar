MAX_N = 10000
ID_LEN = 5
n = 2
primes = []
string = ""
while len(string) < MAX_N + ID_LEN:
  iscomposite = False
  for p in primes:
    if 0 == n % p:
      iscomposite = True
      break
  if not(iscomposite):
    primes.append(n)
    string += str(n)
  n += 1

def solution(i): return string[i:i+5]