const assetConditions = {
  0: {
    value: 0,
    description: "Not Set"
  },
  1: {
    value: 1,
    description: "Brand New"
  },
  2: {
    value: 2,
    description: "Good"
  }
}

const getAssetConditions = assetConditions => {
  descriptions = []
  for (const key in assetConditions){
    descriptions.push(assetConditions[key].description)
  }
  return descriptions
}


console.log(getAssetConditions(assetConditions))