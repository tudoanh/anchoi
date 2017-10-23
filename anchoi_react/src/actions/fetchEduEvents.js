export const FETCH_EDU_EVENTS_START = 'FETCH_EDU_EVENTS_START'
export const fetchEduEventsStart = () => (
  {
    type: FETCH_EDU_EVENTS_START,
  }
)

export const FETCH_EDU_EVENTS_ERROR = 'FETCH_EDU_EVENTS_ERROR'
export const fetchEduEventsError = (err) => (
  {
    type: FETCH_EDU_EVENTS_ERROR,
    payload: err
  }
)

export const FETCH_EDU_EVENTS_SUCCESS = 'FETCH_EDU_EVENTS_SUCCESS'
export const fetchEduEventsSuccess = (data) => (
  {
    type: FETCH_EDU_EVENTS_SUCCESS,
    payload: data
  }
)
