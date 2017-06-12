import React from 'react'

import ViewDependencies from 'viewDependencies'

import Background from './components/background/component'

import Login from './components/apps/login'
import Wall from './components/apps/wall'
import Game from './components/apps/game'
import Archive from './components/apps/archive'
import Community from './components/apps/community'

import Profile from './components/modals/profile'
import Account from './components/modals/account'
import Rank from './components/modals/rank'
import PrivateRace from './components/modals/privateRace'

class View extends React.Component{
  render(){
    let controller = this.props.controller
    let data = this.props.model.data
    let state = this.props.model.state
    return(
      <div>
        <ViewDependencies/>
        <Background/>

        {/* App */}
        {state.app == "login" && <Login data={data} state={state} controller={controller}/>}
        {state.app == "wall" && <Wall data={data} state={state} controller={controller}/>}
        {state.app == "game" && <Game data={data} state={state} controller={controller}/>}
        {state.app == "archive" && <Archive data={data} state={state} controller={controller}/>}
        {state.app == "community" && <Commmunity data={data} state={state} controller={controller}/>}

        {/* Modal */}
        {state.modal == "profile" && <Profile data={data} state={state} controller={controller}/>}
        {state.modal == "account" && <Account data={data} state={state} controller={controller}/>}
        {state.modal == "rank" && <Rank data={data} state={state} controller={controller}/>}
        {state.modal == "private" && <PrivateRace data={data} state={state} controller={controller}/>}

      </div>
    )
  }
}

export default View
