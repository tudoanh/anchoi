import React, { Component } from 'react'
import { Link } from 'react-router-dom'


export class ListHeading extends Component {
  render () {
    return (
      <div>
        <div className="columns is-mobile">
          <div className="column is-10-desktop">
            <h1 className="title is-size-4-mobile">
              {this.props.children}
            </h1>
          </div>
          <div className="column">
            <div className="group is-pulled-right">
              <div className="icon">
                <i className="fa fa-list-alt" aria-hidden="true"></i>
              </div>
              <Link to="" className="see-all">
                <span>Xem thêm</span>
              </Link>
            </div>
          </div>
        </div>
      </div>
    )
  }
}
