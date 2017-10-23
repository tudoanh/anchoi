import { connect } from 'react-redux'
import axios from 'axios'
import { MovieList } from '../components/MovieList'
import * as actions from '../actions/fetchMovieEvents'


const mapStateToProps = (state) => ({
  data: state.getIn(['movieEvents']),
  API_URL: state.getIn(['baseCity', 'API_URL']),
  startTime: state.getIn(['dateRange', 'startTime']),
  endTime: state.getIn(['dateRange', 'endTime'])
})

const mapDispatchToProps = (dispatch) => (
  {
    fetch: (API_URL, startTime, endTime) => (
      dispatch(actions.fetchMovieEventsStart()),
      axios.get(`${API_URL}&since_0=${startTime}&since_1=${endTime}&order=attending_count&category=movie`)
                  .then(response => dispatch(actions.fetchMovieEventsSuccess(response.data)))
                  .catch(e => dispatch(actions.fetchMovieEventsError(e)))
    )
  }
)


const MovieListContainer = connect(mapStateToProps, mapDispatchToProps)(MovieList)

export default MovieListContainer
