import React, { Component } from 'react'
import {
  Link
} from 'react-router-dom'

import { setCity } from '../actions/setCity'


export const NavBar = () =>
  <nav className='navbar' aria-label="main navigation">
    <div className='navbar-brand'>
      <Link to='/' className='navbar-item'>
        <img alt='' src={require('../anchoi_logo_2.png')} />
      </Link>
    </div>
    <div className='navbar-menu'>
      <div className='navbar-end'>
        <div className='navbar-item has-dropdown is-hoverable'>
          <a className='navbar-link'>Thành phố</a>
          <div className="navbar-dropdown">
            <Link
              to='/hanoi'
              className='navbar-item'
            >
              Hà Nội
            </Link>
            <Link
              to='/saigon'
              className='navbar-item'
            >
              Sài Gòn
            </Link>
          </div>
        </div>
        <Link to='/help' className='navbar-item is-active'>
          Hỗ trợ
        </Link>
        <Link to='/signup' className='navbar-item is-active'>
          Đăng ký
        </Link>
        <Link to='/login' className='navbar-item is-active'>
          Đăng nhập
        </Link>
      </div>
    </div>
  </nav>
