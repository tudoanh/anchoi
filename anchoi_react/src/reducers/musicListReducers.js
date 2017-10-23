import Immutable from 'immutable'


const initialState = Immutable.fromJS({
  fetching: false,
  fetched: false,
  error: null,
  events: [],
  nextHref: null,
  prevHref: null,
  count: null,
})

export const fetchMusicEventsReducer = (state=initialState, action) => {
  switch (action.type) {
    case 'FETCH_MUSIC_EVENTS_START':
      return state.set('fetching', true)
    case 'FETCH_MUSIC_EVENTS_ERROR':
      return state.set('error', action.payload)
    case 'FETCH_MUSIC_EVENTS_SUCCESS':
      return state
        .set('fetching', false)
        .set('fetched', true)
        .set('events', action.payload.results)
        .set('nextHref', action.payload.next)
        .set('prevHref', action.payload.previous)
        .set('count', action.payload.count)
    default:
      return state
  }
}
