function solution(progresses, speeds) {
	let prog = [...progresses];
	let speed = [...speeds];
	let ans = [];

	while (prog.length > 0) {
		let cnt = 0;

		while (prog.length > 0 && prog[0] < 100) {
			prog.forEach((v, idx) => {
				prog[idx] += speed[idx];
			});
		}

		while (prog.length > 0 && speed.length > 0 && prog[0] >= 100) {
			prog.shift();
			speed.shift();
			cnt += 1;
		}

		ans.push(cnt);
	}

	return ans;
}
