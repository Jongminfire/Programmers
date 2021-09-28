function solution(enter, leave) {
	let answer = new Array(enter.length).fill(0);
	let dic = {};
	let room = [enter.shift()];

	for (let i = 1; i <= enter.length + 1; i++) {
		dic[i] = new Set();
	}

	while (enter.length > 0 && leave.length > 0) {
		while (room.indexOf(leave[0]) === -1) {
			room.push(enter.shift());
		}

		room.forEach((v) => {
			room.forEach((v2) => {
				if (v !== v2) {
					dic[v].add(v2);
				}
			});
		});

		room.splice(room.indexOf(leave[0]), 1);
		leave.shift();
	}

	for (let v of Object.keys(dic)) {
		answer[v - 1] = dic[v].size;
	}

	return answer;
}
