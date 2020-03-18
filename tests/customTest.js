const add = (a, b) => a + b;

it("adds two numbers", () => {
  const result = add(1, 2);
  const expectedResult = 3;

  expect(result).toEqual(expectedResult);
});

// adds two numbers: PASS/FAIL

function it(description, fn) {
  try {
    fn();
    console.log(`${description}: PASS`);
  } catch {
    console.log(`${description}: FAIL`);
  }
}

// function expect(result) { // result = 3

//   return {
//     toEqual: function(expectedResult) {
//       if(expectedResult === result){
//           return true;
//       } else{
//          return false;
//       }

//     }
//   }
// }

const expect = actual => ({
  toEqual: expected => {
    console.log(expected);
    console.log(actual);
    if (actual === expected) {
      return true;
    } else throw new Error();
  }
});
