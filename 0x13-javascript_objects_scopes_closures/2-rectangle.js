#!/usr/bin/node
class Rectangle {
    //empty class
    constructor(w, h){
        if (!(w <= 0 || h <= 0)){
            this.width = w;
            this.height = h;
        }
    }
}
