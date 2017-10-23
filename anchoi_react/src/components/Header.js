import React, { Component } from 'react'


export class Header extends Component {
  render () {
    return (
      <section className="hero">
        <div className="hero-body">
          <div className="container">
            <h1 className="title is-1" style={{color: '#FF5A5F'}}>
              Ăn & chơi
            </h1>
            <h2 className="subtitle is-3">
              Find amazing events and try unique experiences <br/>
              with awesome people in your area.
            </h2>
          </div>
        </div>
      </section>
    )
  }
}
