#!/usr/bin/node
class Rectangle {
    //empty class
    constructor(w, h){
        if (!(w <= 0 || h <= 0)){
            this.width = w;
            this.height = h;
        }
    }
    print() {
        let i, j;
        for (i = 0; i < this.height; i++){
            for (j = 0; j < this.width; j++){
                console.log("X");
            }
            console.log("\n");
        }
    }
}