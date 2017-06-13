import React from 'react'
import Container from 'container'

class Navbar extends Container{
  render(){
    return(
      <div className={"wall-navbar"}>
        <NavBarLogo/>
        <div className={"wall-navbar-button-container"}>
          <NavBarButton name={"Tutorial"} action={()=>{}}/>
          <NavBarButton name={"Why u"} action={()=>{}}/>
          <NavBarButton name={"Calculator"} action={()=>{}}/>
          <NavBarButton name={"Reset"} action={()=>{}}/>
          <NavBarButton name={"New ticket"} action={()=>{}}/>
        </div>
      </div>
    )
  }
}

export default Navbar

const NavBarLogo = (props) => (
  <p className={"wall-navbar-logo"}>Sherwood<span id={"bet"}>BET</span></p>
)

const NavBarButton = (props) => (
  <button
    className={"sherwood-button navbar-button"}
    onClick={props.action}>{props.name}
  </button>
)
