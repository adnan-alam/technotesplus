<template>
  <div>
    <b-row class="mb-4">
      <b-col cols="12" md="6">
        <b-button
          class="text-right"
          variant="primary"
          @click="showAddNoteModal"
        >
          Add Note
        </b-button>
      </b-col>
    </b-row>
    <b-row v-if="note.notesCount > 0">
      <b-col v-for="element in note.notesList" :key="element.id" cols="12">
        <note-card :note-data="element"></note-card>
      </b-col>
      <b-col>
        <b-pagination
          v-model="currentPage"
          :total-rows="note.notesCount"
          :per-page="pageSize"
          @change="fetchNoteList"
        ></b-pagination>
      </b-col>
    </b-row>
    <b-row v-else>
      <b-col cols="12">
        <b-alert variant="info" show>No record available</b-alert>
      </b-col>
    </b-row>

    <add-note></add-note>

    <edit-note></edit-note>
  </div>
</template>

<script>
import { mapState } from "vuex";
import AddNote from "./AddNote.vue";
import NoteCard from "./NoteCard.vue";
import EditNote from "./EditNote.vue";

export default {
  props: ["searchTerm"],

  components: {
    AddNote,
    EditNote,
    NoteCard,
  },

  data() {
    return {
      pageSize: 2,
      currentPage: 1,
    };
  },

  created() {
    this.fetchNoteList(1);
  },

  computed: {
    ...mapState(["note"]),
  },

  methods: {
    fetchNoteList(currentPage) {
      this.$store.dispatch("note/fetchUserNotesList", {
        pageSize: this.pageSize,
        page: currentPage,
        searchTerm: this.searchTerm,
      });
    },

    showAddNoteModal() {
      this.$bvModal.show("modal_add_note");
    },
  },
};
</script>

<style></style>
