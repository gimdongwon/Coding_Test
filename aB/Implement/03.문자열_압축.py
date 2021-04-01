def solution(s):
  answer = len(s)
  step = 1
  
  while step < len(s) // 2 + 1:
    dup_cnt = 1 
    comp_str = ''
    prev_str = s[0:step]
    
    for idx in range(step, len(s) + step, step):
      now_str = s[idx : idx + step]
      if prev_str == now_str:
        dup_cnt += 1
      else:
        comp_str += prev_str if dup_cnt == 1 else str(dup_cnt) + prev_str   
        dup_cnt = 1
      prev_str = now_str
    
    answer = min(answer, len(comp_str))
    step += 1
  return answer
  