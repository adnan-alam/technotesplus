import Vue from "vue";
import NoteService from "../service/NoteService.js";

export const namespaced = true;

export const state = {
  notesList: [],
  notesCount: null,
  selectedNote: null,
  tagsList: [],
};

export const mutations = {
  SET_NOTES_LIST(state, notesList) {
    state.notesList = notesList;
  },

  SET_NOTES_COUNT(state, notesCount) {
    state.notesCount = notesCount;
  },

  SET_SELECTED_NOTE(state, note) {
    state.selectedNote = note;
  },

  ADD_NOTE(state, note) {
    state.notesList.unshift(note);
  },

  EDIT_NOTE(state, note) {
    state.notesList = state.notesList.filter((element) => {
      if (element.slug == note.slug) {
        element.id = note.id;
        element.slug = note.slug;
        element.title = note.title;
        element.content = note.content;
        element.tags = note.tags;
        element.created_at = note.created_at;
        element.modified_at = note.modified_at;
      }
      return element;
    });
  },

  DELETE_NOTE(state, noteSlug) {
    state.notesList = state.notesList.filter((element) => {
      if (element.slug !== noteSlug) {
        return element;
      }
    });
  },

  SET_TAGS_LIST(state, tagsList) {
    state.tagsList = tagsList;
  },
};

export const actions = {
  fetchUserNotesList({ commit }, { pageSize, page, searchTerm }) {
    return NoteService.fetchUserNotesList(pageSize, page, searchTerm)
      .then((response) => {
        commit("SET_NOTES_LIST", response.data.results);
        commit("SET_NOTES_COUNT", response.data.count);
        return response;
      })
      .catch((err) => {
        console.log(err);
        return err.response;
      });
  },

  fetchUserNote({}, noteSlug) {
    return NoteService.fetchUserNote(noteSlug)
      .then((response) => {
        return response;
      })
      .catch((err) => {
        console.log(err);
        return err.response;
      });
  },

  addUserNote({ commit }, note) {
    return NoteService.addUserNote(note)
      .then((response) => {
        commit("ADD_NOTE", response.data);
        Vue.toasted.show("Note added successfully", {
          className: "bg-success",
        });
        return response;
      })
      .catch((err) => {
        console.log(err);
        return err.response;
      });
  },

  editUserNote({ commit }, { noteSlug, note }) {
    return NoteService.editUserNote(noteSlug, note)
      .then((response) => {
        commit("EDIT_NOTE", response.data);
        Vue.toasted.show("Note updated successfully", {
          className: "bg-success",
        });
        return response;
      })
      .catch((err) => {
        console.log(err);
        return err.response;
      });
  },

  deleteUserNote({ commit }, noteSlug) {
    return NoteService.deleteUserNote(noteSlug)
      .then((response) => {
        commit("DELETE_NOTE", noteSlug);
        Vue.toasted.show("Note deleted successfully", {
          className: "bg-danger",
        });
        return response;
      })
      .catch((err) => {
        console.log(err);
        return err.response;
      });
  },

  fetchTagsList({ commit }) {
    return NoteService.fetchTagsList()
      .then((response) => {
        commit("SET_TAGS_LIST", response.data);
        return response;
      })
      .catch((err) => {
        console.log(err);
        return err.response;
      });
  },
};
