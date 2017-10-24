import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import moment from 'moment'
import Truncate from 'react-truncate'

import { NavBar } from './NavBar'
import { RelatedEvents } from './RelatedEvents'
import { Divider } from './Divider'
import { Footer } from './Footer'


const API_URL = 'http://128.199.215.162:8000/api/v1.0/events/'
const GOOGLE_API_KEY = 'AIzaSyDPtbGItw64sLl0XmfegIW3FE48nyfLBq4'


export class EventDetail extends Component {
  constructor(props) {
    super(props)
    this.state = {
      event: {},
      expanded: false,
      truncated: false
    }

    this.fetchEventData.bind(this)
    this.setEventData.bind(this)
    this.handleTruncate = this.handleTruncate.bind(this);
    this.toggleLines = this.toggleLines.bind(this);
  }

  handleTruncate(truncated) {
    if (this.state.truncated !== truncated) {
      this.setState({
        truncated
      })
    }
  }

  toggleLines(event) {
    event.preventDefault()
    this.setState({
      expanded: !this.state.expanded
    })
  }

  fetchEventData(id) {
    fetch(`${API_URL}${id}`)
      .then(response => response.json())
      .then(result => this.setEventData(result))
      .catch(e =>e)
  }

  setEventData(result) {
    this.setState({result})
  }

  componentDidMount() {
    this.fetchEventData(this.props.match.params.id)
  }


  render () {
    const { result, expanded, truncated} = this.state
    const data = ( result && result.data ) || {}
    const latitude = (result && result.latitude) || ''
    const longitude = (result && result.longitude) || ''
    let mapUrl = `https://maps.googleapis.com/maps/api/staticmap?zoom=17&maptype=roadmap&markers=icon:https://i.imgur.com/MKelSUu.png|${latitude},${longitude}&size=600x600&key=${GOOGLE_API_KEY}`
    const place = (result && result.data && result.data.place) || {}
    const location = (place && place.location) || {}
    console.log(location)

    return (
      <div>
        {
          ('name' in data)
            ? (
              <div>
                <div style={{paddingTop: '50px'}} className="columns">
                  <div className="column is-4 is-offset-2 is-10-mobile is-offset-1-mobile">
                    <h1 className="title is-2 is-size-4-mobile">{data.name}</h1>
                    <Divider />
                    <div className="columns">
                      <div className="column is-3">
                        <h3 className="title is-4">Thời gian bắt đầu</h3>
                      </div>
                      <div className="column">
                        {('ticket_uri' in data)
                          ? <a href={data.ticket_uri} className="button is-primary">
                              <span className="icon">
                                <i className="fa fa-ticket" aria-hidden="true"></i>
                              </span>
                              <span>Mua vé</span>
                            </a>
                          : null
                        }
                        <div style={{paddingTop: '10px'}} className="group">
                          <span className="icon">
                            <i className="fa fa-calendar-o" aria-hidden="true"></i>
                          </span>
                          <span className='is-size-5'>
                            {moment(data.start_time).format('dddd, DD-MM-YYYY')}
                          </span>
                        </div>
                        <div style={{paddingTop: '10px'}} className="group">
                          <span className="icon">
                            <i className="fa fa-clock-o" aria-hidden="true"></i>
                          </span>
                          <span className='is-size-5'>
                            {moment(data.start_time).format('HH:mm')}
                          </span>
                        </div>
                      </div>
                    </div>
                    {('description' in data)
                        ?  <div>
                            <Divider />
                            <div className="columns">
                              <div className="column is-3">
                                <h3 className="title is-4">Chi tiết</h3>
                              </div>
                              <div className="column">
                                <div className="content">
                                  <Truncate
                                    lines={!expanded && 5}
                                    ellipsis={(
                                      <span>... <a href='' onClick={this.toggleLines}>Đọc tiếp</a></span>
                                    )}
                                    onTruncate={this.handleTruncate}
                                  >
                                    {data.description.split('\n').map((item, i) =>
                                      <p key={i}>
                                        {item}
                                      </p>)
                                    }
                                  </Truncate>
                                  {!truncated && expanded && (
                                    <span><a href='' onClick={this.toggleLines}>Thu gọn</a></span>
                                  )}
                                </div>
                              </div>
                            </div>
                          </div>
                        : null
                      }
                    {('end_time' in data)
                      ? <div>
                          <Divider />
                          <div className="columns">
                              <div className="column is-3">
                                <h3 className="title is-4">Thời gian kết thúc</h3>
                              </div>
                              <div className="column">
                                <div className="group">
                                  <span className="icon">
                                    <i className="fa fa-calendar-times-o" aria-hidden="true"></i>
                                  </span>
                                  <span className='is-size-5'>{moment(data.end_time).format('DD-MM-YYYY')}</span>
                                </div>
                                <div className="group">
                                  <span className="icon">
                                    <i className="fa fa-lock" aria-hidden="true"></i>
                                  </span>
                                  <span className='is-size-5'>{moment(data.end_time).format('HH:mm')}</span>
                                </div>
                              </div>
                            </div>
                        </div>
                      : null
                    }
                    <Divider />
                    <div className="columns">
                      <div className="column is-3">
                        <div className="title is-4">
                          Địa điểm
                        </div>
                      </div>
                      <div className="column">
                        {(Object.keys(place).length !== 0)
                          ? <div className="group">
                              <span className="icon">
                                <i className="fa fa-map-marker" aria-hidden="true"></i>
                              </span>
                              <span className='is-size-5'>{place.name}</span>
                            </div>
                          : null
                        }
                        {(Object.keys(location).length !== 0)
                          ? <div>
                              <div className="group">
                                  <span className="icon">
                                    <i className="fa fa-location-arrow" aria-hidden="true"></i>
                                  </span>
                                  <span className="is-size-5">{location.street}</span>
                                </div>
                                <div className="group">
                                    <span className="icon">
                                      <i className="fa fa-plane" aria-hidden="true"></i>
                                    </span>
                                    <span className="is-size-5">{location.city}</span>
                                  </div>
                            </div>
                          : null
                        }
                        {latitude
                          ? <div style={{paddingTop: '10px'}}>
                              <figure className='image is-square'>
                                <img alt='' src={mapUrl} />
                              </figure>
                            </div>
                          : null
                        }
                      </div>
                    </div>
                  </div>
                  <div style={{paddingLeft: '20px', paddingRight: '20px'}} className='column is-4'>
                    <figure className='image'>
                      <img alt='' style={{borderRadius: '8px'}} src={data.cover.source} />
                    </figure>
                    <div style={{paddingTop: '20px'}} className="columns">
                      <div className="column is-6">
                        <div>
                          <span className="is-size-5">
                            Tham dự: {data.attending_count}+
                          </span>
                        </div>
                        <div style={{paddingTop: '10px'}}>
                          <span className="is-size-5">
                            Đang quan tâm: {data.maybe_count}+
                          </span>
                        </div>
                      </div>
                      <div className="column">
                        {('ticket_uri' in data)
                          ? <a href={data.ticket_uri} className="button is-primary is-pulled-right is-large is-hidden-mobile">
                              <span className="icon">
                                <i className="fa fa-ticket" aria-hidden="true"></i>
                              </span>
                              <span>Mua vé</span>
                            </a>
                          : null
                        }
                      </div>
                    </div>
                  </div>
                </div>
                {/*<div style={{paddingTop: '20px'}} className="container">
                  <h1 className="title is-3">Các sự kiện thú vị khác</h1>
                  <RelatedEvents />
                </div>*/}
              </div>
            )
            : null
        }
        <Footer />
      </div>
    )
  }
}
