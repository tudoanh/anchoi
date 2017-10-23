export const FETCH_EXPERIENCE_EVENTS_START = 'FETCH_EXPERIENCE_EVENTS_START'
export const fetchExperienceEventsStart = () => (
  {
    type: FETCH_EXPERIENCE_EVENTS_START,
  }
)

export const FETCH_EXPERIENCE_EVENTS_ERROR = 'FETCH_EXPERIENCE_EVENTS_ERROR'
export const fetchExperienceEventsError = (err) => (
  {
    type: FETCH_EXPERIENCE_EVENTS_ERROR,
    payload: err
  }
)

export const FETCH_EXPERIENCE_EVENTS_SUCCESS = 'FETCH_EXPERIENCE_EVENTS_SUCCESS'
export const fetchExperienceEventsSuccess = (data) => (
  {
    type: FETCH_EXPERIENCE_EVENTS_SUCCESS,
    payload: data
  }
)
