function a() {
  function b() {
    function c() {
      return greeting;
    }
    return c();
  }
  return b();
}

const greeting = "hello";

console.log(a());
