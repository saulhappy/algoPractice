const nums = [1, 2, 3, 4];

const transformation = (num) => num * 2;

const arrayReducer = (nums, transformation) => {
  let result = [];

  for (let i = 0; i < nums.length; i++) {
    result.push(transformation(nums[i]));
  }

  return result;
};

console.log(arrayReducer(nums, transformation));
