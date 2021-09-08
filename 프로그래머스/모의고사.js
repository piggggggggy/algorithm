// 모의고사
// 문제 설명
// 수포자는 수학을 포기한 사람의 준말입니다. 
// 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 
// 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

// 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
// 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
// 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

// 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
// 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

// 제한 조건
// 시험은 최대 10,000 문제로 구성되어있습니다.
// 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
// 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

function solution(answers) {
  let answer = [];
  
  let first = [];
  for (let i = 0;i<2000;i++) {
      first[5*i] = 1;
      first[5*i + 1] = 2;
      first[5*i + 2] = 3;
      first[5*i + 3] = 4;
      first[5*i + 4] = 5;
  };
  let second = [];
  for (let i = 0;i<1250;i++) {
      second[8*i] = 2;
      second[8*i + 1] = 1;
      second[8*i + 2] = 2;
      second[8*i + 3] = 3;
      second[8*i + 4] = 2;
      second[8*i + 5] = 4;
      second[8*i + 6] = 2;
      second[8*i + 7] = 5;
  };
  let third = [];
  for (let i = 0;i<1000;i++) {
      third[10*i] = 3;
      third[10*i + 1] = 3;
      third[10*i + 2] = 1;
      third[10*i + 3] = 1;
      third[10*i + 4] = 2;
      third[10*i + 5] = 2;
      third[10*i + 6] = 4;
      third[10*i + 7] = 4;
      third[10*i + 8] = 5;
      third[10*i + 9] = 5;
  };
  
  let answer1 = 0
  let answer2 = 0
  let answer3 = 0
  
  for (let i=0;i<answers.length;i++) {
      if (answers[i] === first[i]) {
          answer1 += 1;
      }
      if (answers[i] === second[i]) {
          answer2 += 1;
      }
      if (answers[i] === third[i]) {
          answer3 += 1;
      }
  }
  
  const maxx = Math.max(answer1, answer2, answer3);
  
  if (maxx === answer1) {
      answer.push(1);
  }
  if (maxx === answer2) {
      answer.push(2);
  }
  if (maxx === answer3) {
      answer.push(3);
  }
  
  return answer;
}

// 조금 부끄러운풀이............................