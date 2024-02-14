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
    rotate(){
        let x;
        x = this.height
        this.height = this.width;
        this.width = x;
    }
    double(){
        this.height = 2 * this.height;
        this.width = 2 * this.width;
    }
}