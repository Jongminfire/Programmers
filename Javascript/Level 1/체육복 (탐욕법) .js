function solution(n, lost, reserve) {
	let arr = new Array(n + 1).fill(true);
	let res = new Set(reserve.sort());
	let answer = 0;

	lost.sort();
	lost.forEach((v) => (arr[v] = false));

	res.forEach((v) => {
		if (!arr[v]) {
			arr[v] = true;
		} else if (!arr[v - 1] && v - 1 > 0 && !res.has(v - 1)) {
			arr[v - 1] = true;
		} else if (!arr[v + 1] && v + 1 <= n && !res.has(v + 1)) {
			arr[v + 1] = true;
		}
	});

	return arr.filter((v) => v).length - 1;
}

// 기존 하드코딩 풀이 고차함수 활용해서 다시 풀었음
