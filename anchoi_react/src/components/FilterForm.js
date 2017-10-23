import React, { Component } from 'react'


export class FilterForm extends Component {
  render () {
    return (
      <div style={{paddingBottom: '30px'}}>
        <div className="field is-horizontal">
          <div className="field-body">
            <div className="field">
              <div className="control">
                <input className="input is-large" type="text" placeholder="Tên hoặc từ khóa" />
              </div>
            </div>
            <div className="field">
            <div className="control">
              <button className="button is-large is-primary">
                Tìm kiếm
              </button>
            </div>
          </div>
          </div>
        </div>
      </div>
    )
  }
}
