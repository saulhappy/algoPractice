const items = [1, 2, 3];

const i = 1;

console.log(items.slice(0, i));
console.log(items.slice(i + 1));

const x = [items.slice(0, i)] + [items.slice(i + 1)];

const y = [];

y.push(parseInt(x[0]));

console.log(y);
