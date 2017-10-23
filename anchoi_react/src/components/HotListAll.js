import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import InfiniteScroll from 'react-infinite-scroller'

import { NavBar } from './NavBar'
import { Header } from './Header'
import { FilterForm } from './FilterForm'
import { NormalItem } from './NormalItem'


const API_URL = 'http://128.199.215.162:8000/api/v1.0/events/'


export class HotListAll extends Component {
  constructor (props) {
    super(props)
    this.state = {
      events: [],
      hasMore: true,
      nextHref: null
    }

    this.setEvents.bind(this)
  }

  fetchEvents() {
    let url = API_URL
    if (this.state.nextHref) {
      url = this.state.nextHref
    }

    fetch(url)
      .then(response => response.json())
      .then(
        results => this.setEvents(results)
      )
      .catch(e => e)
  }

  setEvents(results) {
    if (results) {
      let {events} = this.state
      results.results.map(event => events.push(event))
      results.next
        ? this.setState({nextHref: results.next})
        : this.setState({hasMore: false})
    }
  }

  render () {
    let list = (this.state.events) || []

    return (
      <div>
        <NavBar />

        <div className="container">
          <Header />
          <div style={{paddingLeft: '20px', paddingRight: '20px'}}>
            <section className="hero">
              <div className="hero-body">
                <div className="container">
                  <h1 className="title is-3">
                    Các sự kiện nổi bật
                  </h1>
                </div>
              </div>
            </section>
            <InfiniteScroll
                  pageStart={0}
                  loadMore={this.fetchEvents.bind(this)}
                  hasMore={this.state.hasMore}
            >
              <div className="columns is-multiline">
                { list.length?
                  list.map( item =>
                    ('cover' in item.data)?
                      <div key={item.fb_id} className="column is-3">
                        <NormalItem
                          src={item.data.cover.source}
                          title={item.name}
                          href={item.fb_id}
                        />
                      </div>
                      : null
                  )
                  : null}
              </div>
            </InfiniteScroll>
          </div>
        </div>
      </div>
    )
  }
}
