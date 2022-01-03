function solution(n, s) {
	let answer = n <= s ? new Array(n - (s % n)).fill(Math.floor(s / n)) : [-1];

	if (n > s || s % n === 0) {
		// n이 s보다 크거나 s가 n으로 나누어 지는 경우
		return answer;
	} else {
		return [...answer, ...new Array(s % n).fill(Math.floor(s / n) + 1)];
	}
}
