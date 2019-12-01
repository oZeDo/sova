import axios from 'axios'

export const BASE_URL = 'http://167.172.165.25:8091/get_dishes'
export const API_URL = BASE_URL

const API = axios.create({
  baseURL: API_URL
})

export default API
