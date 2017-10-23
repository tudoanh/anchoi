import React, { Component } from 'react'


export class Footer extends Component {
  render () {
    return (
      <footer className="footer">
        <div className="container">
          <div className="content has-text-centered">
            <h1 className='title'>
              Mabe by <a href="https://github.com/tudoanh">me</a> with <i style={{color: '#FF5A5F'}} className="fa fa-heart" aria-hidden="true"></i>
            </h1>
          </div>
        </div>
      </footer>
    )
  }
}
