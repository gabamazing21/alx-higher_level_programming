#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square{
    constructor(size)
    {
        super(size, size);
    }
    charPrint(c){
        if (c !== undefined){
            let i, j;
            for (i = 0; i < this.height; i++){
                for (j = 0; j < this.width; j++){
                    console.log(c);
                }
                console.log("\n");
            }
        }
        else{
            super.print();
        }
    }
}