let intervalId = null;
let counter = 0

function printName() {
    if(counter < 5){
        counter++
        console.log("Saul")
    } else{
        console.log(intervalId)
        clearInterval(intervalId)
    }
}

intervalId = setInterval(printName, 1000);
