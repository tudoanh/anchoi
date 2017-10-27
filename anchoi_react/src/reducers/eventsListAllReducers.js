import Immutable from 'immutable'
import * as actions from '../actions/setEventsListAll'


const initialState = Immutable.fromJS({})


export const eventsListAllReducer = (state=initialState, action) => {
  switch (action.type) {
    case actions.SET_EVENTS:
      return state.set(action.payload.category, action.payload.events)
    case actions.UPDATE_EVENTS:
      return state.update(action.payload.category, l => l.push(action.payload.events))
    default:
      return state
}}
