import React from 'react'
import Container from 'container'

class Modal extends Container{
  constructor(props){
    super(props)
  }
  content(){
    return(
      <div>
        Empty modal
      </div>
    )
  }
  setStyle(){
    return {
      width: "40%",
      left: "30%",
      top: "10vh"
    }
  }
  componentWillMount(){
    this.modalContent = this.content(this.props)
  }
  componentDidMount(){
    this.modal = document.getElementById("sherwood-modal")
    this.background = document.getElementById("sherwood-modal-background")
  }
  componentWillReceiveProps(nextProps){
    this.modalContent = this.content(nextProps)
  }
  close(){
    this.modal.classList.add('sherwood-modal-leave')
    this.background.classList.add('sherwood-modal-background-leave')
    setTimeout(() => {this.dispatch({type: "MODAL_CLOSED"})}, 500)
  }
  render(){
    return(
      <div>
        <div id={"sherwood-modal"} className={"sherwood-modal"} style={this.setStyle()}>
          <div
            id={"sherwood-modal-content-container"}
            className={"sherwood-modal-content-container"}>
            {this.modalContent}
          </div>
        </div>
        <div id={"sherwood-modal-background"} className={"sherwood-modal-background"}></div>
      </div>
    )
  }
}

export default Modal
