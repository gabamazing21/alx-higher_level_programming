#!/usr/bin/node
const argv = process.argv.slice(2);
if (argv.length <= 0 ) {
    console.log(0);
}
  else {
    console.log(findSecondInt(argv));
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
