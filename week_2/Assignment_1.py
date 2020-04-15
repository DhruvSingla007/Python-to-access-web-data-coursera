import re as re
handle = open('regex_sum_404116.txt','r')

ans = 0
for line in handle:
    line = line.rstrip()
    nums = re.findall('[0-9]+',line)
    if len(nums) == 0: continue
    for num in nums:
        val = int(num)
        ans = ans + val

print(ans)

