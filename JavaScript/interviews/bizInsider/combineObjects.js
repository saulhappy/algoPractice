// b. Write a function that combines two objects and
//    adds an additonal attribute favoriteAnimal: 'Elephant'.

const obj1 = { age: "22", favoriteColor: "purple" };
const obj2 = { firstName: "John", lastName: "Smith" };

function combineObjectsAndAddAttribute(obj1, obj2) {
  return {
    ...obj1,
    ...obj2,
    favoriteAnimal: "Elephant",
  };
}

console.log(combineObjectsAndAddAttribute(obj1, obj2));
