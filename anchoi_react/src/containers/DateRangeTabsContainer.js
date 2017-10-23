import { connect } from 'react-redux'
import { DateRangeTabs } from '../components/DateRangeTabs'
import {
  setDateRangeToday,
  setDateRangeWeekend,
  setDateRangeThisWeek,
  setDateRangeThisMonth
} from '../actions/setDateRange'


const mapStateToProps = state => ({
  startTime: state.getIn(['dateRange', 'startTime']),
  endTime: state.getIn(['dateRange', 'endTime']),
  activeIndex: state.getIn(['dateRange', 'activeIndex'])
})


const mapDispatchToProps = dispatch => (
  {
    setDateRangeToday: idx => (
      dispatch(setDateRangeToday(idx))
    ),
    setDateRangeWeekend: idx => (
      dispatch(setDateRangeWeekend(idx))
    ),
    setDateRangeThisWeek: idx => (
      dispatch(setDateRangeThisWeek(idx))
    ),
    setDateRangeThisMonth: idx => (
      dispatch(setDateRangeThisMonth(idx))
    )
  }
)

const DateRangeTabsContainer = connect(mapStateToProps, mapDispatchToProps)(DateRangeTabs)


export default DateRangeTabsContainer
