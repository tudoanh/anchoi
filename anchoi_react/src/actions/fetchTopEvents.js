export const FETCH_TOP_EVENTS_START = 'FETCH_TOP_EVENTS_START'
export const fetchTopEventsStart = (eventType) => (
  {
    type: `${eventType}/${FETCH_TOP_EVENTS_START}`,
    eventType
  }
)

export const FETCH_TOP_EVENTS_ERROR = 'FETCH_TOP_EVENTS_ERROR'
export const fetchTopEventsError = (eventType, err) => (
  {
    type: `${eventType}/${FETCH_TOP_EVENTS_ERROR}`,
    payload: err,
    eventType
  }
)

export const FETCH_TOP_EVENTS_SUCCESS = 'FETCH_TOP_EVENTS_SUCCESS'
export const fetchTopEventsSuccess = (eventType, data) => (
  {
    type: `${eventType}/${FETCH_TOP_EVENTS_SUCCESS}`,
    payload: data,
    eventType
  }
)

const eventsType = ['movieEvents', 'musicEvents', 'sportEvents', 'experienceEvents', 'eduEvents']
