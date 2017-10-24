import {
  SET_DATE_RANGE_TODAY,
  SET_DATE_RANGE_WEEKEND,
  SET_DATE_RANGE_THIS_WEEK,
  SET_DATE_RANGE_THIS_MONTH
} from '../actions/setDateRange'
import moment from 'moment'
import Immutable from 'immutable'


let currentDate = moment().format('YYYY-MM-DD')
const dateFormat = 'YYYY-MM-DD'


const initialState = Immutable.fromJS({
  activeIndex: 0,
  startTime: currentDate,
  endTime: moment().endOf('month').format(dateFormat)
})


const dateRangeReducer = (state=initialState, action) => {
  switch (action.type) {
    case SET_DATE_RANGE_TODAY:
      return state
        .set('activeIndex', action.payload)
        .set('startTime', currentDate)
        .set('endTime', currentDate)
    case SET_DATE_RANGE_WEEKEND:
      return state
        .set('activeIndex', action.payload)
        .set('startTime', moment().day(6).format(dateFormat))
        .set('endTime', moment().day(7).format(dateFormat))
    case SET_DATE_RANGE_THIS_WEEK:
      return initialState
    case SET_DATE_RANGE_THIS_MONTH:
      return state
        .set('activeIndex', action.payload)
        .set('startTime', currentDate)
        .set('endTime', moment().endOf('month').format(dateFormat))
    default:
      return state
  }
}

export default dateRangeReducer
