// --- Directions
// Check to see if two provided strings are anagrams of each other. One string is an anagram of another if it uses the same characters in the same quantity. Only consider characters, not spaces or punctuation.  Consider capital letters to be the same as lower case
// --- Examples
//   anagrams('rail safety', 'fairy tales') --> True
//   anagrams('RAIL! SAFETY!', 'fairy tales') --> True
//   anagrams('Hi there', 'Bye there') --> False

let stringA = "RAIL! safety!!";
let stringB = "fairy tales";
let stringC = "HI THERE!!!";

// SOLUTION 1
function anagrams(stringA, stringB) {
  // first, remove special characters, set to lower case
  stringA = stringA.replace(/[^\w]/g, "").toLocaleLowerCase();
  stringB = stringB.replace(/[^\w]/g, "").toLocaleLowerCase();

  // then, if lengths are not the same, return false, else, create character maps of vthe strings to compare values

  if (stringA.length != stringB.length) {
    return false;
  } else {
    stringACharMap = {};
    stringBCharMap = {};
    for (let char of stringA) {
      stringACharMap[char] = stringACharMap[char] + 1 || 1;
    }
    for (let char of stringB) {
      stringBCharMap[char] = stringBCharMap[char] + 1 || 1;
    }
    // compare key:value pairs.
    for (let char in stringACharMap) {
      if (stringACharMap[char] != stringBCharMap[char]) {
        return false;
      } else {
        return true;
      }
    }
  }
}

// SOLUTION 2: using helper function, comparing key length, and not creating new variable for cleaned string

function anagrams(stringA, stringB) {
  const aCharMap = buildCharMap(stringA);
  const bCharMap = buildCharMap(stringB);
  if (Object.keys(aCharMap).length != Object.keys(bCharMap).length) {
    return false;
  }
  for (let char in aCharMap) {
    if (aCharMap[char] !== bCharMap[char]) {
      return false;
    }
  }
  return true;
  function buildCharMap(str) {
    const charMap = {};
    for (let char of str.replace(/[^\w]/g, "").toLocaleLowerCase()) {
      charMap[char] = charMap[char] + 1 || 1;
    }
    return charMap;
  }
}

// SOLUTION 3: Using sort by splitting string to array, then joining, then comparing again.
function anagrams(stringA, stringB) {
  return cleanString(stringA) === cleanString(stringB);
}
function cleanString(str) {
  return str
    .replace(/[^\w]/g, "")
    .toLowerCase()
    .split("")
    .sort()
    .join("");
}
anagrams(stringA, stringB);
