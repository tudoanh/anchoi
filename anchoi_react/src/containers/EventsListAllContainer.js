import { connect } from 'react-redux'
import axios from 'axios'
import { EventsListAll } from '../components/EventsListAll'
import * as actions from '../actions/setEventsListAll'


const mapStateToProps = (state, ownProps) => ({
  data: state.getIn(['eventsListAll']),
  API_URL: state.getIn(['baseCity', 'API_URL']),
  startTime: state.getIn(['dateRange', 'startTime']),
  endTime: state.getIn(['dateRange', 'endTime']),
  ...ownProps
})


const mapDispatchToProps = (dispatch, ownProps) => (
  {
    fetchEvents: (url, startTime, category, endTime) => (
      dispatch(actions.fetchEventsStart()),
      axios.get(`${url}&since_0=${startTime}&since_1=${category !== 'all'? '' : endTime}&order=attending_count&category=${category !== 'all'? category : ''}`)
        .then(response => dispatch(actions.fetchEventsSuccess(response.data, category)))
        .catch(e => dispatch(actions.fetchEventsError(e)))
    )
  }
)


const EventsListAllContainer = connect(mapStateToProps, mapDispatchToProps)(EventsListAll)

export default EventsListAllContainer
