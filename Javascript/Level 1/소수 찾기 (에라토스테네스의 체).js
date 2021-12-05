function solution(n) {
	let answer = 0;
	let arr = Array(n).fill(true);

	// 에라토스테네스의 체 사용
	for (let i = 2; i <= Math.sqrt(n); i++) {
		if (arr[i]) {
			let j = 2;

			while (i * j <= n) {
				arr[i * j] = false;
				j += 1;
			}
		}
	}

	for (let i = 2; i <= n; i++) {
		if (arr[i]) answer += 1;
	}

	return answer;
}
