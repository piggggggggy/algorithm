function solution(nums) {
  
  const set_nums = new Set (nums);
  const setted_nums = [...set_nums]
  let answer = 0;
  let check_nums = nums.length

  if (setted_nums.length >= check_nums/2) {
    answer = check_nums/2;
  }else {
    answer = setted_nums.length;
  }

  return answer;
}

console.log(solution([1,2,2,3,3,5,6]))