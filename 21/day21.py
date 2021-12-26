import sys

infile = sys.argv[1] if len(sys.argv) > 1 else '21.in'
a, b = map(lambda x:int(x.split(' ')[-1]), open(infile).read().strip().split('\n'))
a -= 1; b-=1;

sa = sb = 0 # initial scores
c = 0  # number of dice rolls
d = 1 # curr dice position
i = 0 # counter to update a's or b's score
while sa < 1000 and sb < 1000:
    if i < 3:
        a = (a+d)%10
    else: 
        b = (b+d)%10

    c += 1 
    d = d+1 if d+1 <= 100 else (d+1)%100
    i+=1

    if i == 3:
        sa += a+1
    if i == 6:
        sb += b+1
        i = 0

print(c * min(sa,sb))

# DISCLAIMER: the solution for this part of the problem was inspired by 
# jonathan paulson's (very neat) recursive brute force/ memoization solution 

states = {} # memoization dict 
def count_win(a, b, sa, sb):
  if sa >= 21:
    return (1,0)
  if sb >= 21:
    return (0,1)

  # stop recursion if game state was already visited
  if (a, b, sa, sb) in states:
    return states[(a, b, sa, sb)]

  ans = (0,0)
  for d1 in [1,2,3]:
    for d2 in [1,2,3]:
      for d3 in [1,2,3]:
        new_a = (a+d1+d2+d3)%10
        new_sa = sa + new_a + 1

        x1, y1 = count_win(b, new_a, sb, new_sa)
        ans = (ans[0]+y1, ans[1]+x1)

  states[(a, b, sa, sb)] = ans
  return ans

a, b = map(lambda x:int(x.split(' ')[-1]), open(infile).read().strip().split('\n'))
a -= 1; b-= 1;
print(max(count_win(a, b, 0, 0)))
