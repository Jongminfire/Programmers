function check(num) {
	let cnt = 0;

	for (let i = 1; i <= num; i++) {
		if (num % i === 0) {
			cnt += 1;
		}
	}

	return cnt % 2 ? false : true;
}

function solution(left, right) {
	let answer = 0;

	for (let i = left; i <= right; i++) {
		answer += check(i) ? i : -i;
	}

	return answer;
}
