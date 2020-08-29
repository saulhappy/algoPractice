// PROBLEM: Write a custom reduce function that takes in an array of nums and a function.
const arrayReducer = (nums, transformation) => {};

// TEST TO VERIFY CORRECTNESS;
describe("4. Write a custom reduce function.", () => {
  it("Mapping function should return [2,4,6,8]", () => {
    const nums = [1, 2, 3, 4];
    assert.deepEqual(
      arrayReducer(nums, (num) => num * 2),
      [2, 4, 6, 8]
    );
  });
  it("Mapping function should return [3,4,5,6]", () => {
    const nums = [1, 2, 3, 4];
    assert.deepEqual(
      arrayReducer(nums, (num) => num + 2),
      [3, 4, 5, 6]
    );
  });
  it("Mapping function should return [-1,0,1,2]", () => {
    const nums = [1, 2, 3, 4];
    assert.deepEqual(
      arrayReducer(nums, (num) => num - 2),
      [-1, 0, 1, 2]
    );
  });
});

// SAUL'S PORTION:

const nums = [1, 2, 3, 4];

const arrayReducer = (nums, transformation) => {
  let result = 0;

  for (let i = 0; i < nums.length; i++) {
    result += nums[i] (transformation); // how do you abstract away the transformation piece to be able add, subtract, multiply, etc?
  }

  return result;
};

console.log(arrayReducer(nums, //??? how do you even call this function?))
