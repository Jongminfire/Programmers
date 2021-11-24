function solution(arr) {
	let min = Math.min(...arr);
	let answer = arr.filter((v) => v != min);
	return answer.length > 0 ? answer : [-1];
}
