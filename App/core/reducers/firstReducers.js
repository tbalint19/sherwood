export const firstReducer = (current, action) => {
  let nextState = Object.assign({}, current)
  console.log("first triggered")
  return nextState
}

export const secondReducer = (current, action) => {
  let nextState = Object.assign({}, current)
  console.log("second triggered")
  return nextState
}
