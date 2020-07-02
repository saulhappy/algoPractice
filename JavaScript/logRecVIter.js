const str = "howdy planet";

function readCharRec(str, i) {
  if (i === str.length) {
    return;
  } else {
    console.log(str[i]);
    readCharRec(str, i + 1);
  }
}

readCharRec(str, 0);

function readCharIter(str) {
  for (let i = 0; i < str.length; i++) {
    console.log(str[i]);
  }
}

readCharIter(str);
