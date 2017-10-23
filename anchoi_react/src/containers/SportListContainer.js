import { connect } from 'react-redux'
import axios from 'axios'
import { SportList } from '../components/SportList'
import * as actions from '../actions/fetchSportEvents'


const mapStateToProps = (state) => ({
  data: state.getIn(['sportEvents']),
  API_URL: state.getIn(['baseCity', 'API_URL']),
  startTime: state.getIn(['dateRange', 'startTime']),
  endTime: state.getIn(['dateRange', 'endTime'])
})

const mapDispatchToProps = (dispatch) => (
  {
    fetch: (API_URL, startTime, endTime) => (
      dispatch(actions.fetchSportEventsStart()),
      axios.get(`${API_URL}&since_0=${startTime}&since_1=${endTime}&order=attending_count&category=sport`)
                  .then(response => dispatch(actions.fetchSportEventsSuccess(response.data)))
                  .catch(e => dispatch(actions.fetchSportEventsError(e)))
    )
  }
)


const SportListContainer = connect(mapStateToProps, mapDispatchToProps)(SportList)

export default SportListContainer
