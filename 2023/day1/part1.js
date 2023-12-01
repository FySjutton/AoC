const fs = require('fs');
const path = require('path');
var total = 0;

fs.readFile(path.join(__dirname, 'data.txt'), 'utf8', (err, data) => {
    for (x of data.split('\n')) {
        let new_code = "";
        for (y of x) {
            if (!isNaN(parseFloat(y))) {
                new_code += y;
            }
        }
        total += parseInt(new_code[0] + new_code[new_code.length - 1]);
    }
    console.log(total)
});