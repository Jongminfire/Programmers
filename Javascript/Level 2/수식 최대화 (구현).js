function solution(expression) {
	let answer = 0;
	let num = expression.split(/[^0-9]/g).map((v) => Number(v)); // 정규식으로 숫자만 분리
	let sign = [];
	let orders = [
		["-", "+", "*"],
		["-", "*", "+"],
		["+", "-", "*"],
		["+", "*", "-"],
		["*", "+", "-"],
		["*", "-", "+"],
	];

	// 부호만 분리해서 sign에 저장
	expression.split("").forEach((v) => {
		if (orders[0].indexOf(v) !== -1) {
			sign.push(v);
		}
	});

	orders.forEach((order) => {
		let copy_num = num.slice();
		let copy_sign = sign.slice();

		for (let i = 0; i < 3; i++) {
			while (copy_sign.indexOf(order[i]) !== -1) {
				let idx = copy_sign.indexOf(order[i]);

				if (order[i] === "+") {
					copy_num[idx] += copy_num[idx + 1];
				} else if (order[i] === "-") {
					copy_num[idx] -= copy_num[idx + 1];
				} else if (order[i] === "*") {
					copy_num[idx] *= copy_num[idx + 1];
				}

				// 계산 후 인덱스로 배열 삭제
				copy_sign.splice(idx, 1);
				copy_num.splice(idx + 1, 1);
			}
		}

		answer = Math.max(answer, Math.abs(copy_num[0]));
	});

	return answer;
}
