function solution(nums) {
  
  const set_nums = [...new Set (nums)]
  let answer = 0;
  let check_nums = nums.length

  if (set_nums.length >= check_nums/2) {
    answer = check_nums/2;
  }else {
    answer = set_nums.length;
  }

  return answer;
}

console.log(solution([1,2,2,3,3,5,6]))