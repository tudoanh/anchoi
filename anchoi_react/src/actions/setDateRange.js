export const SET_DATE_RANGE_TODAY = 'SET_DATE_RANGE_TODAY'
export const setDateRangeToday = (idx) => ({
  type: SET_DATE_RANGE_TODAY,
  payload: idx
})


export const SET_DATE_RANGE_WEEKEND = 'SET_DATE_RANGE_WEEKEND'
export const setDateRangeWeekend = (idx) => ({
  type: SET_DATE_RANGE_WEEKEND,
  payload: idx
})


export const SET_DATE_RANGE_THIS_WEEK = 'SET_DATE_RANGE_THIS_WEEK'
export const setDateRangeThisWeek = (idx) => ({
  type: SET_DATE_RANGE_THIS_WEEK,
  payload: idx
})


export const SET_DATE_RANGE_THIS_MONTH = 'SET_DATE_RANGE_THIS_MONTH'
export const setDateRangeThisMonth = (idx) => ({
  type: SET_DATE_RANGE_THIS_MONTH,
  payload: idx
})
