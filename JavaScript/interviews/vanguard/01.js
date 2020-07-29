const b1 = true;
const b2 = false;
const b3 = true;

if ((b1 && b2) || (b2 && b3) || b2) console.log("ok ");
if ((b1 && b2) || (b2 && b3) || b2 || b1) console.log("dokey ");
