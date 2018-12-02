def sol1(lines):
  twos = 0
  threes = 0
  for line in lines:
    chars = {}

    for c in line:
      if c in chars:
        chars[c] += 1
      else:
        chars[c] = 1
    
    twos += 1 if 2 in chars.values() else 0
    threes += 1 if  3 in chars.values() else 0

  return twos * threes


def sol2(lines):
  for i in range(len(lines) - 2):
    done = False
    line1 = lines[i]
    line2 = None
    for j in range(len(lines) - 1):
      if done:
        break

      line2 = lines[j]

      diffs = 0
      for z in range(len(line1)):
        if line1[z] != line2[z]:
          diffs += 1
      
      done = diffs == 1

    if done:
      lines = [line1, line2]
      break
  
  for i in range(len(lines[0])):
    if (lines[0][i] != lines[1][i]):
      return lines[0][0:i] + lines[0][i+1:]


with open('../data/input2.txt') as f:
  lines = sorted(f.readlines())

  print("Solution 1: " + str(sol1(lines)))
  print("Solution 2: " + sol2(sorted(lines)))