//  Coding Test - TripleByte
//  There is an array with nums that are only between 1 and nums.length. However there is a problem.
//  There is a duplicated number in the array, which means that one number also does not show up.
//  Return the sum of the duplicated number and the missing number.
//  For example: input - [4, 3, 3, 1]
//                3 is duplicated, 2 is missing
//                return 3 + 2

function missingNum(nums) {
	let obj = {};
	for (let num of nums) {
		if (obj[num]) {
			obj[num] += 1;
		} else {
			obj[num] = 1;
		}
	}

	let missNum;
	for (let i = 1; i <= nums.length; i++) {
		if (!obj[i]) {
			missNum = i;
		}
	}

	let dupNum = 0;
	for (let num in obj) {
		if (obj[num] > 1) {
			dupNum = +num;
		}
	}

	return missNum + dupNum;
}

console.log(missingNum([4, 3, 3, 1]));
console.log(missingNum([1, 4, 2, 3, 4]));
