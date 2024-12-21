import {readFileSync} from 'fs';

export const readLines = (file) => {
	return readFileSync(file)
		.toString()
		.split('\n')
		.filter((line) => line.length != 0 );
};
