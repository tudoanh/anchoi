import Immutable from 'immutable'
import * as actions from '../actions/eventDetail'


const initialState = Immutable.fromJS({
  eventId: null,
  fetching: false,
  fetched: false,
  data: {},
  error: null
})

export const eventDetailReducer = (state=initialState, action) => {
  switch (action.type) {
    case actions.FETCH_EVENT_DETAIL_START:
      return state.set('fetching', true).set('eventId', action.payload)
    case actions.FETCH_EVENT_DETAIL_ERROR:
      return state.set('error', action.payload)
    case actions.FETCH_EVENT_DETAIL_SUCCESS:
      return state
        .set('fetching', false)
        .set('fetched', true)
        .set('data', action.payload)
    default:
      return state
  }
}
