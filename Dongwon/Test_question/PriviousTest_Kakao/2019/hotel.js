const solution = (x, room_number) => {
  let rooms = new Map(),
    answer = [],
    tt = [];
  for (let i = 0; i < room_number.length; i++) {
    const get_num = rooms.has(room_number[i]);
    if (get_num) {
      let temp = [room_number[i]];
      let number = room_number[i];

      while (true) {
        let idx = number;
        number = rooms.get(idx);
        if (!number) {
          rooms.set(idx, idx + 1);
          answer.push(idx);
          for (let i = 0; i < temp.length; i++) {
            rooms.set(temp[i], idx + 1);
          }
          break;
        }
        temp.push(number);
      }
    } else {
      answer.push(room_number[i]);
      rooms.set(room_number[i], room_number[i] + 1);
    }
  }
  return answer;
};
