function solution(n) {
    var answer = n.toString(3).split('').reverse().join('');
    // toString(3): 3진법 변환 ,
    // split(''): 배열로 변환
    // reverse(): 역순으로 바꾸기
    // join(''): 배열 문자열로 합치기
    
    return Number.parseInt(answer,3);
    // Number.parseInt(answer,3) : 3진법인 answer을 10진수로 만들기
}
