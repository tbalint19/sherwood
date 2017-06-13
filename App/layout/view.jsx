import React from 'react'

import ViewDependencies from 'viewDependencies'

import Background from './background/component'
import NavBar from './navbar/component'

// import Login from './apps/login/component'
// import Wall from './apps/wall/component'
// import Game from './apps/game/component'
// import Archive from './apps/archive/component'
// import Community from './apps/community/component'
// import Admin from './apps/admin/component'
//
// import Profile from './modals/profile/component'
// import Account from './modals/account/component'
// import Rank from './modals/rank/component'
// import PrivateRace from './modals/privateRace/component'

class View extends React.Component{
  render(){
    let controller = this.props.controller
    let data = this.props.model.data
    let state = this.props.model.state
    return(
      <div>
        <ViewDependencies/>

        <Background/>
        <NavBar/>

        {/* App */}
        {/* {state.app == "login" && <Login data={data} state={state} controller={controller}/>}
        {state.app == "wall" && <Wall data={data} state={state} controller={controller}/>}
        {state.app == "game" && <Game data={data} state={state} controller={controller}/>}
        {state.app == "archive" && <Archive data={data} state={state} controller={controller}/>}
        {state.app == "community" && <Commmunity data={data} state={state} controller={controller}/>}
        {state.app == "admin" && <Admin data={data} state={state} controller={controller}/>} */}

        {/* Modal */}
        {/* {state.modal == "profile" && <Profile data={data} state={state} controller={controller}/>}
        {state.modal == "account" && <Account data={data} state={state} controller={controller}/>}
        {state.modal == "rank" && <Rank data={data} state={state} controller={controller}/>}
        {state.modal == "privateRace" && <PrivateRace data={data} state={state} controller={controller}/>} */}

      </div>
    )
  }
}

export default View
