import { createStore } from 'vuex'
import axios from 'axios'
const store = createStore({

    state () {
      return {
        films: [],
        actors:[],
        pages: 0,
        currentPage:1
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
      updateFilm(state,{id,description,}){
        const filmsInCurrentPage = state.films[state.currentPage-1]
        const filmToUpdate=filmsInCurrentPage.find(film=>film.id==id)
        filmToUpdate.description=description
      },
      updateReviewAverage(state,{id,average}){
        const index=state.films[state.currentPage-1].findIndex(film=>film.id==id)
        state.films[state.currentPage-1][index].average=average.toFixed(2)
      },
      setCurrentPage(state,page){
        state.currentPage = page
      }
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
      },
      async updateDetails({commit},{id,description}){
        await axios.patch(`http://127.0.0.1:8000/movie/${id}/`,{
            description:description,
        })
        commit('updateFilm',{id,description})
        },
        async addReview({commit},{id,grade}){
        const response = await axios.post(`http://127.0.0.1:8000/movie/${id}/review`,{
            grade:grade
        })
        commit('updateReviewAverage',{id,average:response.data.grade__avg})
        }
    }
  })

export default store