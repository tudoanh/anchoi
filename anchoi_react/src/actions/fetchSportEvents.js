export const FETCH_SPORT_EVENTS_START = 'FETCH_SPORT_EVENTS_START'
export const fetchSportEventsStart = () => (
  {
    type: FETCH_SPORT_EVENTS_START,
  }
)

export const FETCH_SPORT_EVENTS_ERROR = 'FETCH_SPORT_EVENTS_ERROR'
export const fetchSportEventsError = (err) => (
  {
    type: FETCH_SPORT_EVENTS_ERROR,
    payload: err
  }
)

export const FETCH_SPORT_EVENTS_SUCCESS = 'FETCH_SPORT_EVENTS_SUCCESS'
export const fetchSportEventsSuccess = (data) => (
  {
    type: FETCH_SPORT_EVENTS_SUCCESS,
    payload: data
  }
)
