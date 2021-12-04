function solution(sizes) {
	let bigger = 0;
	let smaller = 0;

	sizes.forEach((v) => {
		bigger = Math.max(Math.max(...v), bigger);
		smaller = Math.max(Math.min(...v), smaller);
	});

	return bigger * smaller;
}
