import { createStore } from 'vuex'
import API from '@/composables/apiClient'

const store = createStore({

    state () {
      return {
        movies: [],
        selectedMovie:null,
        actors:[],
        numberOfPages: 0,
      }
    },

    mutations:{
      setMovies(state,data){
        state.movies=data.results
        state.numberOfPages = Math.ceil(data.numberOfPages/5)
      },
      setMovie(state,movie){
        state.selectedMovie=movie
      },
      setActors(state,actors){
        state.actors=actors
      },
    },

    actions: {
      async fetchMovies({commit},page) {
          const response = await API.fetchMovies(page)
          commit('setMovies',{results:response.results,numberOfPages:response.count,page:page})
      },
      async fetchMovieById({commit},id) {
          const response = await API.fetchMovieById(id)
          commit('setMovie',response)
      },
      async fetchActors({commit}) {
        const response = await API.fetchActors()
        commit('setActors',response)
      },
      async updateDetails({commit},data){
        const response= await API.updateMovieDetails(data)
        commit('setMovie',response)
        },
      async addReview({commit},data){
        const response= await API.addReview(data)
        commit('setMovie',response)
      }
    }
  })

export default store