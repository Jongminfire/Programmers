function solution(n) {
	let dp = [0];
	let cnt = 0;
	let left = 0;
	let right = 0;

	new Array(n)
		.fill(0)
		.map((v, i) => i + 1)
		.forEach((v) => dp.push(dp[dp.length - 1] + v));

	while (right <= n) {
		let temp = dp[right] - dp[left];

		if (temp > n) {
			left += 1;
		} else {
			if (temp === n) cnt += 1;
			right += 1;
		}
	}

	return cnt;
}
