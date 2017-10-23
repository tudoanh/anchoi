export const FETCH_MUSIC_EVENTS_START = 'FETCH_MUSIC_EVENTS_START'
export const fetchMusicEventsStart = () => (
  {
    type: FETCH_MUSIC_EVENTS_START,
  }
)

export const FETCH_MUSIC_EVENTS_ERROR = 'FETCH_MUSIC_EVENTS_ERROR'
export const fetchMusicEventsError = (err) => (
  {
    type: FETCH_MUSIC_EVENTS_ERROR,
    payload: err
  }
)

export const FETCH_MUSIC_EVENTS_SUCCESS = 'FETCH_MUSIC_EVENTS_SUCCESS'
export const fetchMusicEventsSuccess = (data) => (
  {
    type: FETCH_MUSIC_EVENTS_SUCCESS,
    payload: data
  }
)
