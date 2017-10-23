import { connect } from 'react-redux'
import * as setCity from '../actions/setCity'
import { NavBar } from '../components/NavBar'
import { push } from 'react-router-redux'
import { withRouter } from 'react-router-dom'


const mapStateToProps = (state) => ({
  city: state.getIn(['baseCity', 'city']),
  API_URL: state.getIn(['baseCity', 'API_URL'])
})

const mapDispactchToProps = dispatch => (
  {
    setCityToHanoi: () => (
      dispatch(setCity.setCityToHanoi())
    ),
    setCityToSaiGon: () => (
      dispatch(setCity.setCityToSaiGon())
    )
  }
)

const NavContainer = connect(mapStateToProps, mapDispactchToProps)(NavBar)


export default NavContainer
