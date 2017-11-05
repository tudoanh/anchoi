import React from 'react';
import HomeContainer from './containers/HomeContainer'

import {
  Route,
  Redirect
} from 'react-router-dom'

import {NavBar} from './components/NavBar'
import EventDetailContainer from './containers/EventDetailContainer'
import { Footer } from './components/Footer'
import EventsListAllContainer from './containers/EventsListAllContainer'


const App = () =>
  <div>
    <NavBar />
    <Route exact path='/' component={HomeContainer} />
    <Route path='/event/:id' component={EventDetailContainer} />
    <Route path='/:category' component={EventsListAllContainer} />
    <Footer />
  </div>


export default App;
