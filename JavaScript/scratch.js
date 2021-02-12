ar=[1,2,1,2,1,3,2]
n = 7

function sockMerchant(n, ar) {
    let socks = {};
    let pairs = 0;
  for (let element of ar) {
    socks[element] = socks[element] + 1 || 1;
      if (socks[element] % 2 === 0) {
        pairs += 1;
      }
    }
  return pairs;
  }

  console.log(sockMerchant(n, ar))