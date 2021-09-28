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
				dic[v].add(v2);
			});
		});

		room.splice(room.indexOf(leave[0]), 1);
		leave.shift();
	}

	console.log(dic);

	return answer;
}

console.log(solution([1, 3, 2], [1, 2, 3]));
