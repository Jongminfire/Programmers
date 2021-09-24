function changeToGrade(num) {
	if (num >= 2) {
		return 7 - num;
	} else {
		return 6;
	}
}

function solution(lottos, win_nums) {
	let cnt = 0;
	let zeroCnt = 0;

	for (let i = 0; i < 6; i++) {
		let value = lottos[i];

		if (win_nums.includes(lottos[i])) {
			cnt += 1;
		} else if (lottos[i] === 0) {
			zeroCnt += 1;
		}
	}

	return [changeToGrade(cnt + zeroCnt), changeToGrade(cnt)];
}
