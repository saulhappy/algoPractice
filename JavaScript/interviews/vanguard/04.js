class Stack {
  constructor() {
    this.data = [];
  }

  push(record) {
    this.data.push(record);
  }

  pop() {
    return this.data.pop();
  }

  peek() {
    return this.data[this.data.length - 1];
  }
}

let st = new Stack();

st.push(1);
st.push(1.1);
st.push("Z");
st.push("Hello");

st.forEach((e) => console.log(e));
