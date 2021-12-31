function solution(s) {
	let check = 0;
	let ans = true;

	s.split("").forEach((v) => {
		if (v === ")") {
			if (check === 0) ans = false; // return false 할 경우 forEach 내부 함수의 반환이 되기 때문에 ans라는 변수에 값을 넣는다.
			check -= 1;
		} else {
			check += 1;
		}
	});

	return check > 0 ? false : ans;
}
