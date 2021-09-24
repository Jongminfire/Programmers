function solution(nums) {
	const limit = 3000;
	const numsLength = nums.length;
	let arr = new Array(limit).fill(true);
	let ans = 0;

	// 에라토스테네스의 체 (범위 -3000)
	for (let i = 2; i <= Math.sqrt(limit); i++) {
		if (arr[i]) {
			let j = 2;

			while (i * j <= limit) {
				arr[i * j] = false;
				j++;
			}
		}
	}

	// 3가지 수에 대한 합
	for (let a = 0; a < numsLength - 2; a++) {
		for (let b = a + 1; b < numsLength - 1; b++) {
			for (let c = b + 1; c < numsLength; c++) {
				let value = nums[a] + nums[b] + nums[c];
				if (arr[value]) {
					ans += 1;
				}
			}
		}
	}

	return ans;
}
