function solution(absolutes, signs) {
	return absolutes.reduce((acc, cur, idx) => (signs[idx] ? acc + absolutes[idx] : acc - absolutes[idx]), 0);
}
