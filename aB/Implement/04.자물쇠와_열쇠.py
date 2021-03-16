def rotate_key(key):
  return [list(reversed(i)) for i in zip(*key)]

def check_lock(expanded_lock, lock_len):
  for i in range(lock_len):
    for j in range(lock_len):
      if expanded_lock[i + lock_len][j + lock_len] != 1:
        return False
  return True    

def solution(key, lock):
    answer = True
    lock_len = len(lock)
    key_len = len(key)
    
    expanded_lock = [[0] * (lock_len * 3) for _ in range(lock_len * 3)]
    expanded_lock_len = len(expanded_lock)
    
    for i in range(lock_len):
      for j in range(lock_len):
        expanded_lock[i + lock_len][j + lock_len] = lock[i][j]
    
    for _ in range(4):
      key = rotate_key(key)
        
      for i in range(lock_len * 2):
        for j in range(lock_len * 2):
          for k in range(key_len):
            for l in range(key_len):
              expanded_lock[i + k][j + l] += key[k][l]

          if check_lock(expanded_lock, lock_len) == True:
            return True

          for k in range(key_len):
            for l in range(key_len):
              expanded_lock[i + k][j + l] -= key[k][l]
            
  return False
  