const items = [1, 2, 3];
const i = 1;

let newItems = items.slice(0, i).concat(items.pop(i + 1));

console.log(newItems);
