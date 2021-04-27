const getUid = (() => {
    let uid = 0;
    return () => ++uid;
  })();
  
  console.log(getUid());
  console.log(getUid());