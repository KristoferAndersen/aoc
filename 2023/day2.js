import {readLines} from './utils.js';

const limit = {'red': 12, 'green': 13, 'blue': 14};

const solveDay2a = (lines) => {
	let games = {}
	lines.forEach((line) => {
		let game = +line.split(':')[0].split(' ')[1];
		games[game] = line.split(':')[1].split(/[,;] /).reduce((possible, cubes) => {
			cubes = cubes.trim();
			let cubeCount = cubes.split(' ')[0];
			let cubeColor = cubes.split(' ')[1];
			return possible && cubeCount <= limit[cubeColor];
		}, true);
	});

	return Object.keys(games).reduce((acc, game) => games[game] ? acc + parseInt(game) : acc, 0);
};

const solveDay2b = (lines) => {
	let games = [];
	lines.forEach((line) => {
		let game = +line.split(':')[0].split(' ')[1];
		games.push(line.split(':')[1].split(/[,;] /).reduce((greatestColors, cubes) => {
			cubes = cubes.trim();
			let cubeCount = cubes.split(' ')[0];
			let cubeColor = cubes.split(' ')[1];
			
			greatestColors[cubeColor] = Math.max(greatestColors !== undefined ? greatestColors[cubeColor] || 0 : 0, cubeCount)
			return greatestColors;
			
		}, {}));
	});

	return games.map((game) => game.red * game.green * game.blue).reduce((acc, power) => acc + power);
};

const solve = () => {
	const day2 = 'input/day2.txt';
	let lines = readLines(day2);
	
	console.log("Day 2a:", solveDay2a(lines));
	console.log("Day 2b:", solveDay2b(lines));
};

solve();
