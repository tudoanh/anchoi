export const SET_EVENTS = 'SET_EVENTS'
export const setEvents = (category, events) => ({
  type: SET_EVENTS,
  payload: {
    category,
    events
  }
})

export const UPDATE_EVENTS = 'UPDATE_EVENTS'
export const updateEvents = (category, events) => ({
  type: UPDATE_EVENTS,
  payload: {
    category,
    events
  }
})
