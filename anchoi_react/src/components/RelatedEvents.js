import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import Carousel from 'nuka-carousel'

import { TallItem } from './TallItem'



export class RelatedEvents extends Component {
  constructor(props, context) {
    super(props, context)
    this.mixins = [Carousel.ControllerMixin]
    this.state = {isMobileScreen: false}
  }
  componentDidMount() {
    window.addEventListener("resize", this.resize.bind(this))
    this.resize()
  }
  resize() {
    this.setState({isMobileScreen: window.innerWidth <= 760});
  }
  render() {
    return (
      <div>
        <div className='columns' style={{height: '600px'}}>
          <Carousel
            slidesToShow={this.state.isMobileScreen? 1: 4}
            dragging={true}
            swiping={true}
            decorators={[]}
            slidesToScroll={1}
          >
            <div className='column'>
              <TallItem
                src='https://scontent.xx.fbcdn.net/v/t31.0-8/22426382_1541343622570565_1933416086325151088_o.jpg?oh=315aeab67e817e15379123518855a558&oe=5A777CCF'
                title='E.N.G.R - Energy Groove #1'
              />
            </div>
            <div className='column'>
              <TallItem
                src='https://scontent.xx.fbcdn.net/v/t1.0-9/22309002_1875309022783966_8164293118639864511_n.jpg?oh=3ae56a63ae520f26f20b1141fca54e98&oe=5A6F4D7A'
                title='RƯỢU VANG NGON & NHẠC TRỮ TÌNH: Đừng xa em...'
              />
            </div>
            <div className='column'>
              <TallItem
                src='https://scontent.xx.fbcdn.net/v/t31.0-8/p720x720/22050930_1896049957313015_6333621921120404156_o.jpg?oh=5ee8bc307e6e28d9e3111aeb162374b9&oe=5A6FF5A6'
                title='Share The Light Flea Market'
              />
            </div>
            <div className='column'>
              <TallItem
                src='https://scontent.xx.fbcdn.net/v/t31.0-8/q84/p720x720/22137017_1466460586766532_8044612318788550928_o.jpg?oh=1f8143dc80b83a7bc83fde78b09ed7f4&oe=5A85AF01'
                title='Concert: Hymns to the Night #3'
              />
            </div>
            <div className='column'>
              <TallItem
                src='https://scontent.xx.fbcdn.net/v/t31.0-8/p720x720/22339237_346643372413794_2268755450900958848_o.jpg?oh=ad5f31525e15f4e9e53af0db758cc03a&oe=5A74BF5F'
                title='Full Disclosure - Freaky Friday 13th Party'
              />
            </div>
          </Carousel>
        </div>
      </div>
    )
  }
}
