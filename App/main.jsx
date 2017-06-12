import React from 'react'
import ReactDOM from 'react-dom'

require('sherwood_style')
require('./layout/style')

import core from './core/core'
import View from './layout/view'

const app = document.getElementById('app')

const render = () => {
  let controller = core.store
  let model = controller.getState()
  ReactDOM.render(<View model={model} controller={controller}/>, app)
}

core.store.subscribe(render)
render()
