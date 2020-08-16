import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: { searchWord: "" },
  mutations: {
    onSearchWordStateChanged(state, searchWord) {
      state.searchWord = searchWord;
    }
  },
  getters: {
    searchWordState(state) {
      return state.searchWord;
    }
  }
});
