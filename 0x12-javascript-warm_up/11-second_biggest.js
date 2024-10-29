#!/usr/bin/node
const argv = process.argv.slice(2);
let intArgv = [];
if (argv.length <= 0) {
    console.log(0);
}
  else {
    for (let num of argv){
      intArgv.push(Number.parseInt(num));
    }
    console.log(findSecondInt(intArgv));
  }
function findSecondInt(arr){
    let first = -Infinity;
    let second = -Infinity;
    for (let num of arr){
        if (num > first){
            second = first;
            first = num;
        } else if (num > second && num < first){
            second = num;
        }
    }
    return second;
  }
