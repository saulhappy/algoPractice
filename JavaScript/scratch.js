const items = [1, 2, 3];
const i = 1;

// console.log(items.slice(0, i));
// console.log(items.slice(i + 1));

let newItems = items.slice(0, i).concat(items.slice(i + 1));

console.log(newItems);

let newerItems = [...items];

console.log(newerItems, items);
