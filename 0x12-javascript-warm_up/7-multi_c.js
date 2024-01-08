#!/usr/bin/node
const arg = 'C is fun';
let x;
for (x = 0; x < Number(process.argv[2]); x++) {
  console.log(arg);
}
