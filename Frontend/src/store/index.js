import { createStore } from 'vuex'
import axios from 'axios'
const store = createStore({

    state () {
      return {
        films: [],
        actors:[]
      }
    },

    mutations:{
      setFilms(state,data){
        state.films[data.page-1]=data.results
        state.pages=Math.ceil(data.count/5)
      },
      setActors(state,actors){
        state.actors=actors
      },
    },

    actions: {
      async fetchFilms({commit},page) {
        if(!this.state.films[page-1]){
          const response = await axios.get(`http://127.0.0.1:8000/movies/?page=${page}`)
          commit('setFilms',{ results:response.data.results,page:page,count:response.data.count})
        }
      },
      async fetchActors({commit}) {
        const response = await axios.get('http://127.0.0.1:8000/actors/')
        commit('setActors',response.data)
      }
    }
  })

export default store