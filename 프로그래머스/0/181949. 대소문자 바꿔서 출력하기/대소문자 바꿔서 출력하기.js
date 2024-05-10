const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0].split("").map((c) => c === c.toLowerCase() ? c.toUpperCase() : c.toLowerCase())
    console.log(str.join(""))
});