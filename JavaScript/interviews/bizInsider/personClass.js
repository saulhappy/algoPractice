// 5. Write a class extends the Person class and implements a custom function called
//    getFullInfo that returns firstName, lastName, studentId
class Person {
  constructor(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
  }

  getFullName() {
    return this.firstName + " " + this.lastName;
  }
}

class Student extends Person {
  constructor(studentId, firstName, lastName) {
    super(firstName, lastName);
    this.studentId = studentId;
  }

  getFullInfo() {
    return `${this.firstName}, ${this.lastName}, ${this.studentId}`;
  }
}

const student = new Student("123456", "Sally", "Smith");

console.log(student.getFullInfo());
