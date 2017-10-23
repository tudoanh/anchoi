import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import Truncate from 'react-truncate'


export const NormalItem = ({ src, href, title, eventId }) => (
  <div>
    <div className='image is-16by9'>
      <img alt=''
        src={src}
      />
    </div>
    <div className="content">
      <Link to={`/${eventId}`}>
      <h1 style={{paddingTop: '10px'}} className='is-size-5'>
          <Truncate lines={2}>
            {title}
          </Truncate>

      </h1>
      </Link>
    </div>
  </div>
)
