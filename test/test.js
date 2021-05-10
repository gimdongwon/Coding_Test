// const getPermutations = function (arr, selectNumber) {
//   const results = [];
//   if (selectNumber === 1) return arr.map((value) => [value]); // 1개씩 택할 때, 바로 모든 배열의 원소 return

//   arr.forEach((fixed, index, origin) => {
//     const rest = [...origin.slice(0, index), ...origin.slice(index + 1)]; // 해당하는 fixed를 제외한 나머지 배열
//     const permutations = getPermutations(rest, selectNumber - 1); // 나머지에 대해 순열을 구한다.
//     const attached = permutations.map((permutation) => [fixed, ...permutation]); // 돌아온 순열에 대해 떼 놓은(fixed) 값 붙이기
//     results.push(...attached); // 배열 spread syntax 로 모두다 push
//   });

//   return results; // 결과 담긴 results return
// };

// const example = [1, 2, 3, 4];
// const result = getPermutations(example, 2);
// console.log(result);

// function permutation(arr, selectNum) {
//   let result = [];
//   if (selectNum === 1) return arr.map((v) => [v]);

//   arr.forEach((v, idx, arr) => {
//     const fixer = v;
//     const restArr = arr.filter((_, index) => index !== idx);
//     const permuationArr = permutation(restArr, selectNum - 1);
//     const combineFixer = permuationArr.map((v) => [fixer, ...v]);
//     result.push(...combineFixer);
//   });
//   return result;
// }

// console.log(permutation([1, 2, 3, 4], 2));

function combination(arr, selectNum) {
  const result = [];
  if (selectNum === 1) return arr.map((v) => [v]);
  arr.forEach((v, idx, arr) => {
    const fixed = v;
    const restArr = arr.slice(idx + 1);
    const combinationArr = combination(restArr, selectNum - 1);
    const combineFix = combinationArr.map((v) => [fixed, ...v]);
    result.push(...combineFix);
  });
  return result;
}
console.log(combination([1, 2, 3, 4], 5));
