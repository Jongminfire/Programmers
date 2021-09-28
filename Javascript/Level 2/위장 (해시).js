function solution(clothes) {
	let answer = 1;
	let dic = {};

	clothes.forEach((v) => {
		let sort = v[1];

		if (v[1] in dic) {
			dic[v[1]] += 1;
		} else {
			dic[v[1]] = 1;
		}
	});

	// 모든 조합의 개수는 (조합+1)의 곱 - 1
	for (let v of Object.keys(dic)) {
		answer *= dic[v] + 1;
	}

	return answer - 1;
}
