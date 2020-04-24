import math

# h = 3

#    7
#  3   6
# 1 2 4 5

# 1 -> 3
# 2 -> 3
# 3 -> 7
# 4 -> 6
# 5 -> 6
# 6 -> 7
# 7 -> -1

# Convert to level order?

## h = 4

#        15
#    7       14
#  3   6   10  13
# 1 2 4 5 8 9 11 12

# 1  -> 3
# 2  -> 3
# 3  -> 7
# 4  -> 6
# 5  -> 6
# 6  -> 7
# 7  -> 15
# 8  -> 10
# 9  -> 10
# 10 -> 14
# 11 -> 13
# 12 -> 13
# 13 -> 14
# 14 -> 15

def nearest_power_of_2(n):
  return 2 ** math.floor(math.log(n, 2))

# 11
#   11 - 7 -> 4
#   4  - 3 -> 1

# Smallest element in same level as `q`
def level_base(q):
  while True:
    p = nearest_power_of_2(q)
    if (q == 2 * p - 1):
      return int(q)
    q -= p - 1

assert(1 == level_base(5))
assert(3 == level_base(6))
assert(3 == level_base(10))
assert(3 == level_base(13))
assert(7 == level_base(14))

def sibling(q):
  base = level_base(q)
  below = q - base
  above = q + base
  return above if base == level_base(above) else below

assert(13 == sibling(10))
assert(7 == sibling(14))

def parent(h, q):
  isroot = q == 2 ** h - 1
  return -1 if isroot else 1 + max(q, sibling(q))

def solution(h, qs):
  return [parent(h, q) for q in qs]

assert([-1, 7, 6, 3] == solution(3, [7, 3, 5, 1]))
assert([21, 15, 29]  == solution(5, [19, 14, 28]))