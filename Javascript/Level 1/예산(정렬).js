//function solution(d, budget) {
//    var answer = 0;

//    d.sort(function (a, b) {    // d.sort() �� ������ �ȵǴ� ������ ASCII �� �������� �����ϱ� ����.
//        return a - b;           // ���������� return a-b; ���������� return b-a;
//    });

//    for (let i = 0; i < d.length; i++) {
//        if (budget >= d[i]) {
//            budget -= d[i];
//            answer++;
//        }
//    }

//    return answer;
//}

//// https://programmers.co.kr/learn/courses/30/lessons/12982?language=javascript
//// ������������ ���� �� ���� ���� ����