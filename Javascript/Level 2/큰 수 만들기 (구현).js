function solution(number, k) {
	let arr = number.slice().split("");
	let answer = [arr.shift()];

	arr.forEach((v) => {
		while (answer.length > 0 && answer[answer.length - 1] < v && k > 0) {
			k -= 1;
			answer.pop();
		}

		answer.push(v);
	});

	if (k > 0) answer = answer.slice(0, answer.length - k); // k 남으면 answer 자르기

	return answer.join("");
}
