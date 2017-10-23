export const FETCH_MOVIE_EVENTS_START = 'FETCH_MOVIE_EVENTS_START'
export const fetchMovieEventsStart = () => (
  {
    type: FETCH_MOVIE_EVENTS_START,
  }
)

export const FETCH_MOVIE_EVENTS_ERROR = 'FETCH_MOVIE_EVENTS_ERROR'
export const fetchMovieEventsError = (err) => (
  {
    type: FETCH_MOVIE_EVENTS_ERROR,
    payload: err
  }
)

export const FETCH_MOVIE_EVENTS_SUCCESS = 'FETCH_MOVIE_EVENTS_SUCCESS'
export const fetchMovieEventsSuccess = (data) => (
  {
    type: FETCH_MOVIE_EVENTS_SUCCESS,
    payload: data
  }
)
