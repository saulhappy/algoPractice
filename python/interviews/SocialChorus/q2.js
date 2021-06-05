function pn() {
    this.current = 0
    console.log(current)
    this.next = function(){return ++this.current;}
}

