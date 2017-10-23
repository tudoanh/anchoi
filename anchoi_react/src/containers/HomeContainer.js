import { connect } from 'react-redux'
import * as setCity from '../actions/setCity'
import { Home } from '../components/Home'

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

const HomeContainer = connect(mapStateToProps, mapDispactchToProps)(Home)

export default HomeContainer
