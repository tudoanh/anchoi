import { connect } from 'react-redux'
import axios from 'axios'
import { CategoryList } from '../components/CategoryList'
import * as actions from '../actions/fetchTopEvents'


const mapStateToProps = (state, ownProps) => ({
  data: state.getIn([ownProps.eventType]),
  API_URL: state.getIn(['baseCity', 'API_URL']),
  startTime: state.getIn(['dateRange', 'startTime']),
  endTime: state.getIn(['dateRange', 'endTime'])
})

const mapDispatchToProps = (dispatch, ownProps) => (
  {
    fetch: (API_URL, startTime, endTime) => (
      dispatch(actions.fetchTopEventsStart(ownProps.eventType)),
      axios.get(`${API_URL}&since_0=${startTime}&since_1=${endTime}&order=attending_count&category=${ownProps.category}`)
                  .then(response => (dispatch(actions.fetchTopEventsSuccess(ownProps.eventType, response.data)), console.log(`${API_URL}&since_0=${startTime}&since_1=${endTime}&order=attending_count&category=${ownProps.category}`)))
                  .catch(e => dispatch(actions.fetchTopEventsError(ownProps.eventType, e)))
    )
  }
)


const CategoryListContainer = connect(mapStateToProps, mapDispatchToProps)(CategoryList)

export default CategoryListContainer
