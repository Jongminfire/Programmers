function solution(a, b) {
    var answer = 0;

    if (a > b) {
        var swap = a;
        a = b;
        b = swap;
    }

    for (var i = a ; i <= b; i++) {
        answer += i;
    }

    return answer;
}

// https://programmers.co.kr/learn/courses/30/lessons/12912?language=javascript
// �� ���� ���� �� ���� ���� �����ִ� ����