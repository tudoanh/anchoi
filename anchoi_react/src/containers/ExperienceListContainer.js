import { connect } from 'react-redux'
import axios from 'axios'
import { ExperienceList } from '../components/ExperienceList'
import * as actions from '../actions/fetchExperienceEvents'


const mapStateToProps = (state) => ({
  data: state.getIn(['experienceEvents']),
  API_URL: state.getIn(['baseCity', 'API_URL']),
  startTime: state.getIn(['dateRange', 'startTime']),
  endTime: state.getIn(['dateRange', 'endTime'])
})

const mapDispatchToProps = (dispatch) => (
  {
    fetch: (API_URL, startTime, endTime) => (
      dispatch(actions.fetchExperienceEventsStart()),
      axios.get(`${API_URL}&since_0=${startTime}&since_1=${endTime}&order=attending_count&category=experience`)
                  .then(response => dispatch(actions.fetchExperienceEventsSuccess(response.data)))
                  .catch(e => dispatch(actions.fetchExperienceEventsError(e)))
    )
  }
)


const ExperienceListContainer = connect(mapStateToProps, mapDispatchToProps)(ExperienceList)

export default ExperienceListContainer
