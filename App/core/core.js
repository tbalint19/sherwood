import {createStore} from 'redux'
import createApiController from 'datamanager'
import stateTree from './stateTree'

import {
  firstReducer,
  secondReducer
} from './reducers/firstReducers'

const core = (() => {

  const initialState = Object.assign({}, stateTree)

  const reducer = (current = initialState, action) => {
    switch (action.type) {
      case "SOMETHING_HAPPENED":
        return firstReducer(current, action)
      case "SOMETHING_ELSE_HAPPENED":
        return secondReducer(current, action)
      default:
        return Object.assign({}, current)
    }
  }

  const store = createStore(reducer)
  store.JSONtransfer = createApiController(store)

  return {store}

})()

export default core
