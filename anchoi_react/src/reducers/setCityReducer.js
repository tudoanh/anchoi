import Immutable from 'immutable'


const API_URL = 'http://128.199.215.162:8000/api/v1.0/events/'

export const setCityReducer = (state=Immutable.fromJS({}), action) => {
  switch (action.type) {
    case 'SET_CITY_TO_SAIGON':
      return state
         .set('name', 'Ho Chi Minh City')
         .set('API_URL', `${API_URL}?city=Ho Chi Minh City`)
    case 'SET_CITY_TO_HANOI':
    default:
      return state
         .set('name', 'Hanoi')
         .set('API_URL', `${API_URL}?city=Hanoi`)
  }
}
