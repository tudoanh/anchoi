import { connect } from 'react-redux'
import axios from 'axios'
import { EventDetail } from '../components/EventDetail'
import * as actions from '../actions/eventDetail'

const API_URL = 'http://128.199.215.162:8000/api/v1.0/events'

const mapStateToProps = (state) => ({
  data: state.getIn(['eventDetail']),
})

const mapDispatchToProps = (dispatch) => (
  {
    fetch: (eventId) => (
      dispatch(actions.fetchEventDetailStart(eventId)),
      axios.get(`${API_URL}/${eventId}`)
                  .then(response => dispatch(actions.fetchEventDetailSuccess(response.data)))
                  .catch(e => dispatch(actions.fetchEventDetailError(e)))
    )
  }
)


const EventDetailContainer = connect(mapStateToProps, mapDispatchToProps)(EventDetail)

export default EventDetailContainer
