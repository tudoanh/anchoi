import { setCityReducer } from './setCityReducer'
import { fetchHotEventsReducer } from './fetchHotEventsReducer'
import dateRangeReducer from './setDateRangeReducer'
import { combineReducers } from 'redux-immutable'
import { routerReducer } from 'react-router-redux'
import { fetchMovieEventsReducer } from './movieListReducers'
import { fetchMusicEventsReducer } from './musicListReducers'
import { fetchExperienceEventsReducer } from './experienceListReducers'
import { fetchSportEventsReducer } from './sportListReducers'
import { fetchEduEventsReducer } from './eduListReducers'
import { eventsListAllReducer } from './eventsListAllReducers'
import { eventDetailReducer } from './eventDetailReducers'


const rootReducer = combineReducers({
  baseCity: setCityReducer,
  router: routerReducer,
  hot: fetchHotEventsReducer,
  dateRange: dateRangeReducer,
  musicEvents: fetchMusicEventsReducer,
  movieEvents: fetchMovieEventsReducer,
  sportEvents: fetchSportEventsReducer,
  eduEvents: fetchEduEventsReducer,
  experienceEvents: fetchExperienceEventsReducer,
  eventsListAll: eventsListAllReducer,
  eventDetail: eventDetailReducer
})

export default rootReducer
