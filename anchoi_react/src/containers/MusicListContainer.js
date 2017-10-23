import { connect } from 'react-redux'
import axios from 'axios'
import { MusicList } from '../components/MusicList'
import * as actions from '../actions/fetchMusicEvents'


const mapStateToProps = (state) => ({
  data: state.getIn(['musicEvents']),
  API_URL: state.getIn(['baseCity', 'API_URL']),
  startTime: state.getIn(['dateRange', 'startTime']),
  endTime: state.getIn(['dateRange', 'endTime'])
})

const mapDispatchToProps = (dispatch) => (
  {
    fetch: (API_URL, startTime, endTime) => (
      dispatch(actions.fetchMusicEventsStart()),
      axios.get(`${API_URL}&since_0=${startTime}&since_1=${endTime}&order=attending_count&category=music`)
                  .then(response => dispatch(actions.fetchMusicEventsSuccess(response.data)))
                  .catch(e => dispatch(actions.fetchMusicEventsError(e)))
    )
  }
)


const MusicListContainer = connect(mapStateToProps, mapDispatchToProps)(MusicList)

export default MusicListContainer
