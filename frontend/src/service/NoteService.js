import axios from "axios";
import apiClient from "./ApiClient";

// const tokenData = JSON.parse(localStorage.getItem("tokenData"));

// axios.defaults.xsrfCookieName = "csrftoken";
// axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
// if (tokenData) {
//   axios.defaults.headers.common["Authorization"] = `Bearer ${tokenData.access}`;
// }
// const apiClient = axios.create({
//   baseURL: process.env.BASE_URL,
// });

const urlList = {
  rootUrl: "/api/v1/n/",
};

export default {
  fetchUserNotesList(pageSize, page, searchTerm) {
    let url = urlList.rootUrl + `notes/?page_size=${pageSize}&page=${page}`;
    if (searchTerm) {
      url += `&search=${searchTerm}`;
    }
    return apiClient.get(url);
  },

  fetchUserNote(noteSlug) {
    let url = urlList.rootUrl + `notes/${noteSlug}`;
    return apiClient.get(url);
  },

  addUserNote(note) {
    let url = urlList.rootUrl + "notes/";
    return apiClient.post(url, note);
  },

  editUserNote(noteSlug, note) {
    let url = urlList.rootUrl + `notes/${noteSlug}/`;
    return apiClient.patch(url, note);
  },

  deleteUserNote(noteSlug) {
    let url = urlList.rootUrl + `notes/${noteSlug}/`;
    return apiClient.delete(url);
  },

  fetchTagsList() {
    let url = urlList.rootUrl + "tags/";
    return apiClient.get(url);
  },
};
