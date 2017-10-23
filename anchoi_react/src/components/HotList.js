import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import { ListHeading } from './ListHeading'
import { TallItem } from './TallItem'
import Carousel from 'nuka-carousel'

import { store } from '../index'
import { get } from 'immutable'


export class HotList extends Component {
  constructor(props, context) {
    super(props, context)
    this.mixins = [Carousel.ControllerMixin]
    this.state = {isMobileScreen: false}
  }

  componentDidMount() {
    window.addEventListener("resize", this.resize.bind(this))
    this.resize()
    this.props.fetch(
      this.props.API_URL,
      this.props.startTime,
      this.props.endTime
    )
  }

  componentWillReceiveProps(nextProps) {
    if (
      nextProps.endTime !== this.props.endTime
      || nextProps.startTime !== this.props.startTime
      || nextProps.API_URL !== this.props.API_URL
    ) {
      this.props.fetch(
        nextProps.API_URL,
        nextProps.startTime,
        nextProps.endTime
      )
    }
  }

  resize() {
    this.setState({isMobileScreen: window.innerWidth <= 760});
  }

  render () {
    const { data } = this.props
    return (
      <div>
        <ListHeading seeAll={'/hanoi'}>Nổi bật</ListHeading>
          <div className='columns' style={{height: '600px'}}>
            {(data.get('fetched') && data.get('hotEvents').length)
            ? <Carousel
                slidesToShow={this.state.isMobileScreen? 1: 4}
                dragging={true}
                swiping={true}
                decorators={[]}
                slidesToScroll={1}
              >
                { data.get('hotEvents').map((event, i) =>
                    <div key={i} className='column'>
                      <TallItem
                        src={event.data.cover.source}
                        title={event.data.name}
                        eventId={event.id}
                      />
                    </div>
                  )
                }
              </Carousel>
           : null
         }
          </div>
      </div>
    )
  }
}
