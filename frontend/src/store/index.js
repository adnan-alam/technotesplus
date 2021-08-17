import Vue from "vue";
import Vuex from "vuex";

import * as auth from "./auth.js";
import * as note from "./note.js";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: { auth, note },
});
