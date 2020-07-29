const devicenames = ["switch", "switch", "tv", "switch", "tv", "switch", "tv"];

function deviceNameSystem(devicenames) {
  let deviceMap = {};
  let uniqueDevicename = [];

  for (let i = 0; i < devicenames.length; i++) {
    deviceMap[i] = devicenames[i];
  }

  for (let device in deviceMap) {
    debugger;
    uniqueDevicename.push(
      deviceMap[device] + getKeyByValue(deviceMap, devicenames[device])
    );
  }

  function getKeyByValue(object, value) {
    return Object.keys(object).find((key) => object[key] === value);
  }

  return uniqueDevicename;
}

console.log(deviceNameSystem(devicenames));
