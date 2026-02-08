from typing import List
def get_permutations(s: str) -> List[str]:
  n = len(s)
  res = []
  curr = []
  used = [False] * n
  def helper():
    if len(curr) == n:
      res.append("".join(curr))
      return
    for i in range(n):
      if not used[i]:
        res.append(s[i])
        used[i] = True
        helper()
        res.pop()
        used[i] = False
  helper()
  return res

s = "".join(list(range(10))
perms = get_permutations(s)

greatestDiameter, validCount = 0, 0



            
