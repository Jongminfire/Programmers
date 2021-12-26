function solution(word) {
	let answer = 0;
	let arr = [781, 156, 31, 6, 1];
	let alpha = ["A", "E", "I", "O", "U"];

	word.split("").forEach((v, i) => {
		answer += 1;
		if (alpha.indexOf(v) > 0) {
			answer += alpha.indexOf(v) * arr[i];
		}
	});

	return answer;
}
