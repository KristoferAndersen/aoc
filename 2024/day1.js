import {readLines} from './utils.js';

const solveDay1a = (file) => {
	let lines = readLines(file);

	let a = Array(lines.length);
	let b = Array(lines.length);

	for(let i = 0; i < lines.length; i++) {
		let [l, r] = lines[i].split('   ').map(Number);
		a[i] = l;
		b[i] = r;
	}


	a.sort();
	b.sort();

	let sum = 0
	for(let i = 0; i < lines.length; i++) {
		sum += Math.abs(a[i] - b[i]);
	}

	return sum;
}

const solveDay1b = (file) => {
	let lines = readLines(file);
	let countB = new Map();

	let a = Array(lines.length);

	for(let i = 0; i < lines.length; i++) {
		let [l, r] = lines[i].split('   ').map(Number);
		a[i] = l;
		countB[r] = (countB[r] || 0) + 1;
	}

	let score = 0;
	for (const n of a) {
		score += (n * (countB[n] || 0));
	}



	return score;
}

console.log("Day1 A:", solveDay1a('input/day1.txt'));
console.log("Day1 B:", solveDay1b('input/day1.txt'));
