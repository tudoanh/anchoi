import React from 'react';
import HomeContainer from './containers/HomeContainer'

import {
  Route,
  Redirect
} from 'react-router-dom'

import {NavBar} from './components/NavBar'
import {EventDetail} from './components/EventDetail'


const App = () =>
  <div>
    <NavBar />
    <Route exact path='/' component={HomeContainer} />
    <Route path='/:id' component={EventDetail} />
  </div>


export default App;
