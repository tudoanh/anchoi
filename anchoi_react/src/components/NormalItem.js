import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import Truncate from 'react-truncate'


export const NormalItem = ({ src, href, title, eventId }) => (
  <div>
    <figure className='image is-16by9'>
      <img style={{borderRadius: '8px'}} alt='' src={src} onLoad={() => {window.dispatchEvent(new Event('resize'));}} />
    </figure>
    <div className="content">
      <Link to={`/event/${eventId}`}>
        <h1 style={{paddingTop: '10px'}} className='is-size-5'>
            <Truncate lines={2}>
              {title}
            </Truncate>
        </h1>
      </Link>
    </div>
  </div>
)
