import Immutable from 'immutable'


const initialState = Immutable.fromJS({
  fetching: false,
  fetched: false,
  error: null,
  hotEvents: [],
  nextHref: null,
  prevHref: null,
  count: null
})

export const fetchHotEventsReducer = (state=initialState, action) => {
  switch (action.type) {
    case 'FETCH_HOT_EVENTS_START':
      return state.set('fetching', true)
    case 'FETCH_HOT_EVENTS_ERROR':
      return state.set('error', action.payload)
    case 'FETCH_HOT_EVENTS_SUCCESS':
      return state
        .set('fetching', false)
        .set('fetched', true)
        .set('hotEvents', action.payload.results)
        .set('nextHref', action.payload.next)
        .set('prevHref', action.payload.previous)
        .set('count', action.payload.count)
    default:
      return state
  }
}
