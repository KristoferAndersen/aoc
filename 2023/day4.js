import {readLines} from './utils.js';

const getHits = (lines) => {
	let lineHits = [];
	lines.map(line => line.split(': ')[1]).forEach(lineNums => {
		let winMap = lineNums.split(' | ')[0].split(/ +/).reduce((m, n) => {m[n.trim()] = true; return m}, {});
		let hits = lineNums.split(' | ')[1].split(/ +/).filter((n) => winMap[n.trim()]);
		lineHits.push(hits.length);
	});

	return lineHits;
};

const solveDay4a = (lines) => {
	return getHits(lines).filter(hits => hits > 0).reduce((a, b) => a + 2**(b-1), 0);
};

const solveDay4b = (lines) => {
	let lineHits = getHits(lines);
	let winStreaks = [];
	let cards = 0;
	lineHits.forEach((hits) => {
		let cardsInLevel = 1 + winStreaks.length;
		cards = cards + cardsInLevel;

		winStreaks = winStreaks.map(c => c-1).filter(c => c > 0);
		for (const _ of Array(cardsInLevel)) {
			if (hits > 0 ) { winStreaks.push(hits) };
		}
	});

	return cards;
};

const solve = () => {
	const day4 = 'input/day4.txt';
	let lines = readLines(day4);
	console.log("Day 4a:", solveDay4a(lines));
	console.log("Day 4b:", solveDay4b(lines));
};

solve();

