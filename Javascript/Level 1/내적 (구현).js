function solution(a, b) {
	return a.reduce((acc, cur, idx) => acc + a[idx] * b[idx], 0);
}

// reduce 사용, a[idx]*b[idx] 합 구하기
