function solution(s) {
	let ans = [0, 0];

	while (s !== "1") {
		while (s.indexOf("0") !== -1) {
			s = s.replace("0", "");
			ans[1] += 1;
		}

		let temp = s.length;
		s = temp.toString(2);

		ans[0] += 1;
	}

	return ans;
}
