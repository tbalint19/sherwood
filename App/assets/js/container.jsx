import React from 'react'

class Container extends React.Component{
  constructor(props){
    super(props)
    this.controller = props.controller
  }
  dispatch(action){
    this.controller.dispatch(action)
  }
  JSONtransfer(request){
    this.controller.JSONtransfer(request)
  }
}

export default Container
