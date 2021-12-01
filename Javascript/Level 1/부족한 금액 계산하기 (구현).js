function solution(price, money, count) {
	let answer = new Array(count).fill(1).reduce((acc, cur, idx) => acc + (idx + 1) * price, 0) - money;
	return answer >= 0 ? answer : 0;
}
