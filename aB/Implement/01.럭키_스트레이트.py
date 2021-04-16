n = input()
target = str(n)
find_index = (len(target) // 2)

if sum(list(map(int, target[:find_index]))) == sum(list(map(int, target[find_index:]))):
  print('LUCKY')
else:
  print('READY')
  