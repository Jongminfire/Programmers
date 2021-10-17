// 순열 구하기
function permutation(arr, selectNum) {
	let result = [];
	if (selectNum === 1) return arr.map((v) => [v]);

	arr.forEach((v, idx, arr) => {
		const fixer = v;
		const restArr = arr.filter((_, index) => index !== idx);
		const permuationArr = permutation(restArr, selectNum - 1);
		const combineFixer = permuationArr.map((v) => [fixer, ...v]);
		result.push(...combineFixer);
	});
	return result.map((v) => v.join(""));
}

// 소수 판별
function isPrime(num) {
	if (num < 2) {
		return false;
	}

	for (let i = 2; i <= Number(Math.sqrt(num)); i++) {
		if (num % i == 0) {
			return false;
		}
	}
	return true;
}

function solution(numbers) {
	const arr = numbers.split("");
	let permu = new Set();
	let answer = 0;

	for (let size = 1; size <= numbers.length; size++) {
		let temp = permutation(arr, size).map((v) => Number(v));
		temp.forEach((v) => {
			permu.add(v);
		});
	}

	permu.forEach((v) => {
		if (isPrime(v)) {
			answer++;
		}
	});

	return answer;
}
