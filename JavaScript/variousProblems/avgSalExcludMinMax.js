// source: https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

// Given an array of unique integers salary where salary[i] is the salary of the employee i.

// Return the average salary of employees excluding the minimum and maximum salary.

// Example 1:

// Input: salary = [4000,3000,1000,2000]
// Output: 2500.00000
// Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
// Average salary excluding minimum and maximum salary is (2000+3000)/2= 2500
// Example 2:

// Input: salary = [1000,2000,3000]
// Output: 2000.00000
// Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
// Average salary excluding minimum and maximum salary is (2000)/1= 2000

const salary = [6000, 5000, 4000, 3000, 2000, 1000];

function average(salary) {
  newSal = salary.sort((a, b) => a - b);
  newSalFiltered = [];

  for (let i = 1; i < newSal.length - 1; i++) {
    newSalFiltered.push(newSal[i]);
  }

  return newSalFiltered.reduce((a, b) => a + b, 0) / newSalFiltered.length;
}

console.log(average(salary));
