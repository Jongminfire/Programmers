function solution(s) {
	let arr = s.split(" ").map((v) => Number(v));
	return `${Math.min(...arr)} ${Math.max(...arr)}`; // Math.max , Math.min은 문자열도 검사하기 때문에 arr에서 map을 사용해서 Number로 바꿔줄 필요 없음
}
