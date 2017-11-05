export const FETCH_EVENTS_START = 'FETCH_EVENTS_START'
export const fetchEventsStart = () => ({
  type: FETCH_EVENTS_START
})

export const FETCH_EVENTS_ERROR = 'FETCH_EVENTS_ERROR'
export const fetchEventsError = (err) => ({
  type: FETCH_EVENTS_ERROR,
  payload: err
})

export const FETCH_EVENTS_SUCCESS = 'FETCH_EVENTS_SUCCESS'
export const fetchEventsSuccess = (data, category) => ({
  type: FETCH_EVENTS_SUCCESS,
  payload: {
    category,
    data
  }
})
