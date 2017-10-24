import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import Carousel from 'nuka-carousel'

import { ListHeading } from './ListHeading'
import { NormalItem } from './NormalItem'

import BlockUi from 'react-block-ui'
import { Loader, Types } from 'react-loaders'
import 'react-block-ui/style.css'
import 'loaders.css/loaders.min.css'


export class MovieList extends Component {
  constructor(props, context) {
    super(props, context)
    this.mixins = [Carousel.ControllerMixin]
    this.state = {isMobileScreen: false}
    this.toggleBlocking = this.toggleBlocking.bind(this);
    this.setLoaderType = this.setLoaderType.bind(this);
    this.state = {
      blocking: false,
      loaderType: 'line-scale',
    }
  }

  toggleBlocking() {
   this.setState({blocking: !this.state.blocking});
  }

  setLoaderType(e) {
   this.setState({loaderType: e.target.value});
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
  beforeSlide(currentSlide = 0) {
    const list = window.document.querySelector('.slider-list');
    const slidesCount = list.childNodes.length;
    const nextSlide = list.childNodes[(currentSlide + 1) % slidesCount];
    list.style.height = Math.max(list.offsetHeight, nextSlide.offsetHeight) + 'px';
  }
  render () {
    const { data } = this.props
    return (
      <div>
        { data.get('events').length
            ? <div>
                <ListHeading>{this.props.children}</ListHeading>
                <div className='columns' style={{paddingBottom: '15px'}}>
                    {data.get('fetched')
                      ? <Carousel
                        slidesToShow={this.state.isMobileScreen? 1: 3}
                        dragging={true}
                        swiping={true}
                        decorators={[]}
                        slidesToScroll={1}
                        heightMode='max'
                        beforeSlide={this.beforeSlide}
                        initialSlideHeight={300}
                      >
                      { data.get('events').map((event, i) =>
                            <div key={i} className="column">
                              <NormalItem
                                src={event.data.cover.source}
                                title={event.name}
                                eventId={event.id}
                                href={event.fb_id}
                              />
                            </div>
                        )
                      }
                      </Carousel>
                      : null
                    }
                  </div>
                </div>
            : null
          }
      </div>
    )
  }
}
