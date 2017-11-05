import React, { Component } from 'react'
import { Link } from 'react-router-dom'


export const TallItem = ({title, src, eventId}) =>{
  return (
      <div>
        <div className='event-thumbnail'>
          <img alt='' src={src} />
        </div>
        <div className="content">
            <h1 style={{paddingTop: '10px'}} className='is-size-5'>
              <Link to={`/event/${eventId}`}>{title}</Link>
            </h1>
        </div>
      </div>
    )
}
