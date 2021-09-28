function solution(maps) {
	const row = maps[0].length;
	const col = maps.length;
	let answer = 0;
	let visited = Array.from(Array(col), () => new Array(row).fill(0));
	let deque = [];

	if (maps[0][0]) {
		deque.push([0, 0]);
		visited[0][0] = 1;
	}

	while (deque.length > 0) {
		let now = deque.shift();
		let x = now[0];
		let y = now[1];

		let move = [
			[x + 1, y],
			[x - 1, y],
			[x, y + 1],
			[x, y - 1],
		];

		// let 붙이는 것 주의!
		for (let v of move) {
			let nx = v[0];
			let ny = v[1];

			if (nx < 0 || nx >= row || ny < 0 || ny >= col) {
				continue;
			}

			if (maps[ny][nx] && visited[ny][nx] === 0) {
				deque.push([nx, ny]);
				visited[ny][nx] = visited[y][x] + 1;
			}
		}
	}

	return visited[col - 1][row - 1] ? visited[col - 1][row - 1] : -1;
}
