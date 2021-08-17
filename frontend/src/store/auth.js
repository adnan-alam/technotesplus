import AuthService from "../service/AuthService.js";
import axios from "axios";

export const namespaced = true;

export const state = {
  tokenData: null,
};

export const mutations = {
  SET_TOKEN_DATA(state, tokenData) {
    localStorage.setItem("tokenData", JSON.stringify(tokenData));
    state.tokenData = tokenData;
  },

  LOGOUT() {
    localStorage.removeItem("tokenData");
    location.reload();
  },
};

export const actions = {
  loginUser({ commit }, userCredentials) {
    return AuthService.loginUser(userCredentials)
      .then((response) => {
        commit("SET_TOKEN_DATA", response.data);
        return response;
      })
      .catch((err) => {
        console.log(err);
        return err.response;
      });
  },

  registerUser({ commit }, userData) {
    return AuthService.registerUser(userData)
      .then((response) => {
        commit("SET_TOKEN_DATA", response.data);
        Vue.toasted.show("Successfully registered", {
          className: "bg-success",
        });
        return response;
      })
      .catch((err) => {
        console.log(err);
        return err.response;
      });
  },

  refreshToken({ commit }) {
    return AuthService.refreshToken()
      .then((response) => {
        commit("SET_TOKEN_DATA", response.data);
        return response;
      })
      .catch((err) => {
        console.log(err);
        return err.response;
      });
  },

  logoutUser({ commit }) {
    commit("LOGOUT");
  },
};

export const getters = {
  loggedIn(state) {
    return !!state.tokenData;
  },
};
