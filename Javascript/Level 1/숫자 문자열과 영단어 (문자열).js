function solution(s) {
	let alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];

	alpha.forEach((v, i) => {
		while (s.includes(v)) {
			s = s.replace(v, i);
		}
	});

	return Number(s);
}
