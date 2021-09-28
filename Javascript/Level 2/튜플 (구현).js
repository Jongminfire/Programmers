function solution(s) {
	let answer = [];
	let str = s
		.slice(2, s.length - 2)
		.split("},{")
		.sort((a, b) => a.split(",").length - b.split(",").length);

	str.forEach((v) => {
		let temp = v.split(",");

		for (let i = 0; i < temp.length; i++) {
			if (answer.indexOf(Number(temp[i])) === -1) {
				answer.push(Number(temp[i]));
				break;
			}
		}
	});

	return answer;
}
