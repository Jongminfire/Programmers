function solution(n) {
	let dp = [0, 1];

	for (let i = 2; i <= n; i++) {
		dp.push((dp[i - 2] + dp[i - 1]) % 1234567); // 매 dp 값 마다 1234567로 나눈 나머지를 저장함
	}

	return dp[n];
}
