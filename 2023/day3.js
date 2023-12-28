import {readLines} from './utils.js';

const isNum = (c) => {
	return '0' <= c && c <= '9';
};

const isSymbol = (c) => {
	return !isNum(c) && c != '.';
};

const isGear = (c) => {
	return c == '*';
};

const getAdjacent = (lines, x, y, comparator) => {
	let matches = [];
	for (const dy of [-1, 0, 1]) {
		let y2 = y + parseInt(dy);
		if(lines[y2] === undefined) {
			continue;
		}

		for (const dx of [-1, 0, 1]) {
			let x2 = x + parseInt(dx);
			if (lines[y2] === undefined) {
				continue;
			}

			let c = lines[y2][x2];
			if(c !== undefined && comparator(c)) {
				matches.push([x2, y2, c]);
			}
		}
	}

	return matches;
};

const solveDay3a = (lines) => {
	let partNumbers = [];
	for(let y = 0; y < lines.length; y++) {
		let number = '';
		let isPart = false;
		for(let x = 0; x < lines[0].length; x++) {
			let char = lines[y].charAt(x);
			if (isNum(char)) {
				number = number + char;
				isPart = isPart || getAdjacent(lines, x, y, isSymbol).length !== 0;
				if(!isNum(lines[y].charAt(x+1)) && isPart) {
					partNumbers.push(parseInt(number));
				}
			}
			else {
				number = '';
				isPart = false;
			}
		}
	}

	return partNumbers.reduce((acc, partNo) => acc + partNo, 0);
};

const solveDay3b = (lines) => {
	let gearValue = {};
	let sum = 0;
	for(let y = 0; y < lines.length; y++) {
		let number = '';
		let isPart = false;
		let gears = [];
		for(let x = 0; x < lines[0].length; x++) {
			let char = lines[y].charAt(x);
			if (isNum(char)) {
				number = number + char;
				gears.push(...getAdjacent(lines, x, y, isGear));
				if(!isNum(lines[y].charAt(x+1)) && gears.length !== 0) {
					let gear = gears[0];
					let key = gear[0] + gear[1] * 10000;
					if (gearValue[key] === undefined) {
						gearValue[key] = number; 
					}
					else {
						sum += parseInt(gearValue[key]) * parseInt(number);
					}
				}
			}
			else {
				number = '';
				gears = [];
			}
		}
	}

	return sum;
};


const solve = () => {
	const day3 = 'input/day3.txt';
	let lines = readLines(day3);
	
	console.log("Day 3a:", solveDay3a(lines));
	console.log("Day 3b:", solveDay3b(lines));
};

solve();
