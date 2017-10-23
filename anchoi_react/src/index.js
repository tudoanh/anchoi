import 'react-dates/initialize'
import React from 'react'
import { render } from 'react-dom'
import { Provider } from 'react-redux'
import { applyMiddleware, createStore } from 'redux'
import { createLogger } from 'redux-logger'
import thunk from 'redux-thunk'
import rootReducer from './reducers'
import App from './App'
import createHistory from 'history/createBrowserHistory'
import { ConnectedRouter, routerMiddleware } from 'react-router-redux'
import Immutable, { Iterable } from 'immutable'

const stateTransformer = (state) => {
  if (Iterable.isIterable(state)) return state.toJS();
  else return state
}

const logger = createLogger({
  stateTransformer,
})

const history = createHistory()
const middleware = applyMiddleware(thunk, logger, routerMiddleware(history))
export const store = createStore(rootReducer, middleware)

render(
  <Provider store={store}>
    <ConnectedRouter history={history}>
      <App />
    </ConnectedRouter>
  </Provider>,
  document.getElementById('root')
)
