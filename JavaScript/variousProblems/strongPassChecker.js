// source: https://leetcode.com/problems/strong-password-checker/

// A password is considered strong if below conditions are all met:

// It has at least 6 characters and at most 20 characters.
// It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
// It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
// Write a function strongPasswordChecker(s), that takes a string s as input, and return the MINIMUM change required to make s a strong password. If s is already strong, return 0.

// Insertion, deletion or replace of any one character are all considered as one change.

const s = "helloooooworldddd";
// const sSplit = s.match(/[a-z]+|[^a-z]+/gi);

function strongPasswordChecker(s) {
  let charCountTwoPlus = "";
  let lengthMinErrors = 0;
  let lengthMaxErrors = 0;
  let upperCount = (s.match(/[A-Z]/g) || []).length;
  let upperErrorCount = 0;
  let lowerCount = (s.match(/[a-z]/g) || []).length;
  let lowerErrorCount = 0;
  let numCount = s.replace(/\D/g, "").length;
  let numErrorCount = 0;
  let totalErrorCount = 0;

  charCountTwoPlus = consecCounter(s);

  console.log(charCountTwoPlus);

  if (s.length < 6) {
    lengthMinErrors = 6 - s.length;
  }

  if (s.length > 20) {
    lengthMaxErrors = s.length - 20;
  }

  if (upperCount < 1) upperErrorCount++;
  if (lowerCount < 1) lowerErrorCount++;
  if (numCount < 1) numErrorCount++;

  totalErrorCount =
    lengthMinErrors +
    lengthMaxErrors +
    upperErrorCount +
    lowerErrorCount +
    numErrorCount;

  // helper functions:

  function consecCounter(s) {
    let result = "";
    let counter = 1;
    let resultFiltered = "";

    for (let i = 0; i < s.length; i++) {
      if (s[i] === s[i + 1]) {
        counter++;
      } else {
        result += s[i] + counter;
        counter = 1;
      }
    }

    for (let i = 0; i < result.length; i++) {
      if (parseInt(result[i + 1]) > 2) {
        resultFiltered += result[i] + result[i + 1];
      }
    }
    return resultFiltered;
  }
}

strongPasswordChecker(s);