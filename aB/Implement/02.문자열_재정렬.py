strs = input()
target = []
n = 0

for data in strs:
  if data.isalpha():
    target.append(data)
  else:
    n += int(data)

target.sort()

if n != 0:
  target.append(str(n))

print(''.join(target))
