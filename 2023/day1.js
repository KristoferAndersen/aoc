import {readLines} from './utils.js';

const findNum = (line, last) => {
	let num = null;
	for(let i = 0; i < line.length; i++) {
		if(line[i] >= '0' && line[i] <= '9') {
			num = line[i];
			if(!last) { return num; }
		}
	}

	return num;
};

const strToFirstNum = (line) => {
	const numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
	if (line.charAt(0) >= '0' && line.charAt(0) <= '9') {
		return line.charAt(0);
	};

	let n = numbers.findIndex((number) => line.startsWith(number));
	return n >= 0 ? n+1 : null;
};

const findNumWord = (line, last) => {
	let value = null;
	for(let i = 0; i < line.length; i++) {
		let num = strToFirstNum(line.substring(i));
		if(num !== null) {
			value = num;
			if(!last) { return num; }
		}
	};

	return value;
};

const solveDay1a = () => {
	let day1 = 'input/day1.txt';
	let lines = readLines(day1);

	return lines
		.map((line) => findNum(line, false) + findNum(line, true))
		.reduce((acc, lineValue) => acc + Number(lineValue), 0);
};

const solveDay1b = () => {
	let day1 = 'input/day1.txt';
	let lines = readLines(day1);

	return lines
		.map((line) => `${findNumWord(line, false)}${findNumWord(line, true)}`)
		.reduce((acc, value) => acc + Number(value), 0);
};

console.log("Day1 A:", solveDay1a());
console.log("Day1 B:", solveDay1b());
