const arr = [
  "90,google.com",
  "300,yahoo.com",
  "20,sports.yahoo.com",
  "1,wikipedia.org",
  "90,uk.gov",
  "800,korea.gov",
  "927,wookeun-s.com",
  "922,saulito.net",
  "39,google.map.com",
  "20,sports.google.com",
  "2020,facebook.com"
];

// Expected Output
// {
//   "com" : 3396,
//   "google" : 129,
//   "yahoo" : 320,
//   "sports" : 20,
//   "wikipedia": 1,
//   "org" : 1,
//   "uk" : 90,
//   "gov" : 890,
//   "wookeun-s" : 927,
//   "saulito" : 922,
//   "net" : 922,
//   "map" : 39,
//   "facebook" : 2020
// }

function subDomainCounter(arr) {
  const result = {};
  for (let i = 0; i < arr.length; i++) {
    const num = arr[i].split(",")[0];
    const domains = arr[i].split(",")[1].split(".");
    for (const domain of domains) {
      if (result[domain]) {
        result[domain] += parseInt(num);
      } else {
        result[domain] = parseInt(num);
      }
    }
  }
  return result;
}

console.log(subDomainCounter(arr));
