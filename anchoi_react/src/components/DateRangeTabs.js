import React, { Component } from 'react'
import { Link } from 'react-router-dom'


export class DateRangeTabs extends Component {
  constructor(props) {
    super(props)
  }

  render () {
    const { match } = this.props
    const tabsText = ['Tuần này', 'Tháng này', 'Hôm nay', 'Cuối tuần']
    const setDateFuncs = [
      this.props.setDateRangeThisWeek,
      this.props.setDateRangeThisMonth,
      this.props.setDateRangeToday,
      this.props.setDateRangeWeekend,      
    ]
    return (
      <div className="tabs is-medium">
        <ul>
          {
            tabsText.map((item, index) =>
              <li
                key={index}
                className={
                  (index === this.props.activeIndex)
                    ? 'is-active'
                    : null
                }
              >
                <a
                  onClick={() => setDateFuncs[index](index)}
                >
                  {item}
                </a>
              </li>
            )
          }
        </ul>
      </div>
    )
  }
}
