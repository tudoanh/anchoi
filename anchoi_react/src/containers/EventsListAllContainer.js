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
    setEvents: (category, events) => actions.setEvents(category, events),
    updateEvents: (category, events) => actions.updateEvents(category, events)
  }
)


const EventsListAllContainer = connect(mapStateToProps, mapDispatchToProps)(EventsListAll)

export default EventsListAllContainer
