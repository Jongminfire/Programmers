function solution(array, commands) {
    var answer = [];

    for (let i = 0; i < commands.length; i++) {
        var slice = [];

        for (let j = commands[i][0] - 1; j <= commands[i][1] - 1; j++) {
            slice.push(array[j]);
        }

        slice.sort((a, b) => { return a - b; });        // slice.sort(); �ϸ� ���̽� ��� �ȵǴ� ��찡 ����
        answer.push(slice[commands[i][2] - 1]);
    }

    return answer;
}

// https://programmers.co.kr/learn/courses/30/lessons/42748?language=javascript
// �迭 �ڸ��� ����