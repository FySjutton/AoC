const fs = require('fs');
const path = require('path');
var total = 0;

fs.readFile(path.join(__dirname, 'FILENAME.txt'), 'utf8', (err, data) => {
    for (x of data.split('\n')) {
        let letter_str = "";
        let nmb = "";
        const test = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
        for (i of x) {
            if (isNaN(parseFloat(i))) {
                letter_str += i;
            } else {
                nmb += i;
            }
            for (p of Object.keys(test)) {
                if (letter_str.includes(p) && letter_str != "") {
                    nmb += test[p];
                    letter_str = p[p.length - 1];
                }
            }
        }
        total += parseInt(nmb[0] + nmb[nmb.length - 1]);
    }
    console.log(total)
});