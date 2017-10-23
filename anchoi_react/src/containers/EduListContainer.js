import { connect } from 'react-redux'
import axios from 'axios'
import { EduList } from '../components/EduList'
import * as actions from '../actions/fetchEduEvents'


const mapStateToProps = (state) => ({
  data: state.getIn(['eduEvents']),
  API_URL: state.getIn(['baseCity', 'API_URL']),
  startTime: state.getIn(['dateRange', 'startTime']),
  endTime: state.getIn(['dateRange', 'endTime'])
})

const mapDispatchToProps = (dispatch) => (
  {
    fetch: (API_URL, startTime, endTime) => (
      dispatch(actions.fetchEduEventsStart()),
      axios.get(`${API_URL}&since_0=${startTime}&since_1=${endTime}&order=attending_count&category=education`)
                  .then(response => dispatch(actions.fetchEduEventsSuccess(response.data)))
                  .catch(e => dispatch(actions.fetchEduEventsError(e)))
    )
  }
)


const EduListContainer = connect(mapStateToProps, mapDispatchToProps)(EduList)

export default EduListContainer
