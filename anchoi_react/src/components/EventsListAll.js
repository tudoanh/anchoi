import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import InfiniteScroll from 'react-infinite-scroller'

import { NavBar } from './NavBar'
import { Header } from './Header'
import { FilterForm } from './FilterForm'
import { NormalItem } from './NormalItem'


export class EventsListAll extends Component {
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
    let url = `${this.props.API_URL}&since_0=${this.props.startTime}` +
               `&since_1=${this.props.match.params.category !== 'all'? '' : this.props.endTime}&order=attending_count&` +
               `category=${this.props.match.params.category !== 'all'? this.props.match.params.category : ''}`
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

  componentDidMount() {
    this.props.fetchEvents(
      this.props.API_URL,
      this.props.startTime,
      this.props.match.params.category,
      this.props.endTime
    )
  }

  render () {
    console.log(this.props, this.state)
    let list = (this.state.events) || []
    const categories = {
      'movie': 'phim/điện ảnh ',
      'music': 'âm nhạc ',
      'education': 'giáo dục ',
      'experience': 'trải nghiệm ',
      'sport': 'thể thao ',
      'all': ''
    }

    return (
      <div>
        { list.length
        ? <div className="container">
            <Header />
            <div>
              <section className="hero">
                <div className="hero-body">
                  <div className="container">
                    {
                      <h1 className="title is-3">
                        Các sự kiện {categories[this.props.match.params.category]}nổi bật
                      </h1>
                    }
                  </div>
                </div>
               </section>
                <InfiniteScroll
                      pageStart={0}
                      loadMore={this.fetchEvents.bind(this)}
                      hasMore={this.state.hasMore}
                >
                  <div style={{paddingLeft: '20px', paddingRight: '20px'}} className="columns is-multiline">
                      {list.map( item =>
                        ('cover' in item.data)?
                          <div key={item.fb_id} className="column is-3">
                            <NormalItem
                              src={item.data.cover.source}
                              title={item.name}
                              eventId={item.id}
                            />
                          </div>
                          : null
                      )}

                  </div>
                </InfiniteScroll>
            </div>
          </div>
        : null
      }
      </div>
    )
  }
}
