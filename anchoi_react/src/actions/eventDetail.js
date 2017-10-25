export const FETCH_EVENT_DETAIL_START = 'FETCH_EVENT_DETAIL_START'
export const fetchEventDetailStart = (eventId) => ({
  type: FETCH_EVENT_DETAIL_START,
  payload: eventId
})

export const FETCH_EVENT_DETAIL_SUCCESS = 'FETCH_EVENT_DETAIL_SUCCESS'
export const fetchEventDetailSuccess = (data) => ({
  type: FETCH_EVENT_DETAIL_SUCCESS,
  payload: data
})

export const FETCH_EVENT_DETAIL_ERROR = 'FETCH_EVENT_DETAIL_ERROR'
export const fetchEventDetailError = (error) => ({
  type: FETCH_EVENT_DETAIL_ERROR,
  payload: error
})
