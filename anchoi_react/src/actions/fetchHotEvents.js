export const FETCH_HOT_EVENTS_START = 'FETCH_HOT_EVENTS_START'
export const fetchHotEventsStart = () => (
  {
    type: FETCH_HOT_EVENTS_START,
  }
)

export const FETCH_HOT_EVENTS_ERROR = 'FETCH_HOT_EVENTS_ERROR'
export const fetchHotEventsError = (err) => (
  {
    type: FETCH_HOT_EVENTS_ERROR,
    payload: err
  }
)

export const FETCH_HOT_EVENTS_SUCCESS = 'FETCH_HOT_EVENTS_SUCCESS'
export const fetchHotEventsSuccess = (data) => (
  {
    type: FETCH_HOT_EVENTS_SUCCESS,
    payload: data
  }
)
