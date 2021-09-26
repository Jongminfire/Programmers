function solution(s) {
	let lst = [];

	Array.from(s).forEach((v, i) => {
		if (lst.length === 0 || lst[lst.length - 1] !== v) {
			lst.push(v);
		} else {
			lst.pop();
		}
	});

	if (lst.length === 2) {
		if (lst[0] === lst[1]) {
			lst = [];
		}
	}

	return lst.length > 0 ? 0 : 1;
}
