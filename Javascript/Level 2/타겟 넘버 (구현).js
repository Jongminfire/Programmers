function solution(numbers, target) {
	const size = numbers.length;
	let answer = 0;

	const dfs = (num, sum, count) => {
		if (count === size) {
			if (sum === target) {
				answer += 1;
			}
			return;
		}

		dfs(num, sum + num[count], count + 1);
		dfs(num, sum - num[count], count + 1);
	};

	dfs(numbers, 0, 0);

	return answer;
}
