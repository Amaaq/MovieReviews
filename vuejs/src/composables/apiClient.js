
import axios from 'axios'

const baseURL = 'http://localhost:8000/'

const ApiService = axios.create({
  baseURL,
  headers: {
    'Content-Type': 'application/json'
  }
})

class API {

    async fetchMovies(page) {
        try {
          const response = await ApiService.get('movies/',{params:{page}})
          return response.data
        } catch (error) {
          throw new Error(error.response.data.detail || error.message)
        }
      }

    async fetchMovieById(id) {
        try {
          const response = await ApiService.get(`movies/${id}/`)
          return response.data
        } catch (error) {
          throw new Error(error.response.data.detail || error.message)
        }
      }
    
    async fetchActors() {
        try {
          const response = await ApiService.get('actors/')
          return response.data
        } catch (error) {
          throw new Error(error.response.data.detail || error.message)
        }
      }
    
    async updateMovieDetails(data){
        try{
            const response = await ApiService.patch(`movies/${data.movieId}/`,{
                description:data.selectedDescription,
                actors:data.selectedActors
            })
            return response.data
        } catch (error) {
            throw new Error(error.response.data.detail || error.message)
        }
    }

    async addReview(data) {
        try {
          const response = await ApiService.post(`movies/${data.movieId}/add_review/`,{grade:data.grade})
          return response.data
        } catch (error) {
          throw new Error(error.response.data.detail || error.message)
        }
    }
}

export default new API()