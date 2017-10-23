import { connect } from 'react-redux'
import axios from 'axios'
import { HotList } from '../components/HotList'
import * as actions from '../actions/fetchHotEvents'


const mapStateToProps = (state) => ({
  data: state.getIn(['hot']),
  API_URL: state.getIn(['baseCity', 'API_URL']),
  startTime: state.getIn(['dateRange', 'startTime']),
  endTime: state.getIn(['dateRange', 'endTime'])
})

const mapDispatchToProps = (dispatch) => (
  {
    fetch: (API_URL, startTime, endTime) => (
      dispatch(actions.fetchHotEventsStart()),
      axios.get(`${API_URL}&since_0=${startTime}&since_1=${endTime}&order=attending_count`)
                  .then(response => (dispatch(actions.fetchHotEventsSuccess(response.data)), console.log('YOLO!')))
                  .catch(e => dispatch(actions.fetchHotEventsError(e)))
    )
  }
)


const HotListContainer = connect(mapStateToProps, mapDispatchToProps)(HotList)

export default HotListContainer
