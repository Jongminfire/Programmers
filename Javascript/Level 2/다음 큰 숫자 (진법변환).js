function solution(n) {
	let bincnt = n.toString(2).match(/1/g).length; // 정규식 활용, 문자열에서 1을 포함하는 배열의 길이

	while (true) {
		n += 1;

		if (n.toString(2).match(/1/g).length === bincnt) {
			return n;
		}
	}
}
