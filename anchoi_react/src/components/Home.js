import React, { Component } from 'react'
import { Route } from 'react-router-dom'

import HotListContainer from '../containers/HotListContainer'
import DateRangeTabsContainer from '../containers/DateRangeTabsContainer'
import { Header } from './Header'
import { FilterForm } from './FilterForm'
import { DateRangeTabs } from './DateRangeTabs'
import { HotList } from './HotList'
import { CategoryList } from './CategoryList'
import { Footer } from './Footer'
import MovieListContainer from '../containers/MovieListContainer'
import MusicListContainer from '../containers/MusicListContainer'
import ExperienceListContainer from '../containers/ExperienceListContainer'
import SportListContainer from '../containers/SportListContainer'
import EduListContainer from '../containers/EduListContainer'


export class Home extends Component {
  constructor(props) {
    super(props)
  }

  render() {
    return (
      <div>
        <div className='container'>
          <Header />
          <div style={{paddingLeft: '20px', paddingRight: '20px'}}>
            <FilterForm />
            <DateRangeTabsContainer />
            <HotListContainer />
            <MovieListContainer>Phim</MovieListContainer>
            <MusicListContainer>
              Âm nhạc
            </MusicListContainer>
            <EduListContainer>
              Giáo dục
            </EduListContainer>
            <ExperienceListContainer>
              Trải nghiệm
            </ExperienceListContainer>
            <SportListContainer>
              Thể thao
            </SportListContainer>
          </div>
        </div>
        <Footer />
      </div>
    )
  }
}
