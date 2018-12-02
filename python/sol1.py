def sol1(lines):
  return sum(lines)

def sol2(lines):
  i = 0
  curSum = 0
  freqs = set()

  while (curSum not in freqs):
    freqs.add(curSum)
    curSum += lines[i]
    i = (i + 1) % len(lines)

  return curSum

with open('../data/input1.txt') as f:
  lines = [int(x) for x in f.readlines()]
  print("Solution 1: " + str(sol1(lines)))
  print("Solution 2: " + str(sol2(lines)))