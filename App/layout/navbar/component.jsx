import React from 'react'
import Container from 'container'

class Navbar extends Container{
  render(){
    return(
      <div className={"wall-navbar"}>
        <NavBarLogo/>
        <div className={"wall-navbar-button-container"}>
          <NavbarButton action={()=>{}} name={"TBalint19"} icon={"account_box"}/>
          <NavbarButton action={()=>{}} name={"719.9$"} icon={"credit_card"}/>
          <NavbarButton action={()=>{}} name={"Professional"} icon={"trending_up"}/>
          <NavbarButton action={()=>{}} name={"Groups"} icon={"group"}/>
          <NavbarButton action={()=>{}} name={"Help"} icon={"live_help"}/>
          <NavbarButton action={()=>{}} name={"Logout"} icon={"power_settings_new"}/>
        </div>
      </div>
    )
  }
}

export default Navbar

const NavBarLogo = (props) => (
  <div>
    <h1 className={"wall-navbar-logo"}>
      <span id={"logo-sherwood"}>Sherwood</span>
      <span id={"logo-bet"}>BET</span>
    </h1>
  </div>
)

const NavbarButton = (props) => (
  <button
    className={"navbar-button"}
    onClick={props.action}>
    <i className="material-icons md-12 icon-align">{props.icon}</i>
    {props.name}
  </button>
)
