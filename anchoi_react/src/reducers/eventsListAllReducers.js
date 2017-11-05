import Immutable from 'immutable'
import * as actions from '../actions/setEventsListAll'


const initialState = Immutable.fromJS({
  category: null,
  events: [],
  fetching: false,
  fetched: false,
  error: null
})


export const eventsListAllReducer = (state=initialState, action) => {
  switch (action.type) {
    case actions.FETCH_EVENTS_START:
      return state.set('fetching', true)
    case actions.FETCH_EVENTS_ERROR:
      return state
        .set('fetching', false)
        .set('error': action.payload)
    case actions.FETCH_EVENTS_SUCCESS:
      return state
        .set('fetching': false)
        .set('fetched': true)
        .set('category', action.payload.category)
        .set('events', action.payload.data.results)
    default:
      return state
}}
