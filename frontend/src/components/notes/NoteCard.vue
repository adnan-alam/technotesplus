<template>
  <div>
    <b-card class="mb-4" :title="noteData.title">
      <b-card-text v-html="noteData.content"> </b-card-text>
      <a
        v-for="tag in noteData.tags"
        :key="tag.index"
        class="badge bg-secondary text-decoration-none link-light"
        style="margin-right: 5px"
        href="#!"
        >{{ tag }}</a
      >

      <b-row class="my-4">
        <b-col cols="6">
          <b-button
            variant="primary"
            size="sm"
            @click.prevent="onEditNote(noteData)"
          >
            Edit
          </b-button>
        </b-col>
        <b-col cols="6" class="text-right">
          <b-button
            variant="danger"
            size="sm"
            @click="onDeleteNote(noteData.title, noteData.slug)"
          >
            Delete
          </b-button>
        </b-col>
      </b-row>
    </b-card>
  </div>
</template>

<script>
import { mapMutations } from "vuex";

export default {
  props: ["noteData"],

  methods: {
    ...mapMutations("note", ["SET_SELECTED_NOTE"]),

    onEditNote() {
      this.SET_SELECTED_NOTE(this.noteData);
      this.$bvModal.show("modal_edit_note");
    },

    onDeleteNote(title, slug) {
      this.$bvModal
        .msgBoxConfirm(`Confirm delete note - ${title}`, {
          hideHeader: true,
          bodyBgVariant: "danger rounded-top",
          bodyTextVariant: "white",
          size: "md",
          buttonSize: "sm",
          okVariant: "danger",
          okTitle: "Confirm",
          cancelTitle: "Cancel",
          cancelVariant: "primary",
          footerClass: "p-2",
          hideHeaderClose: false,
          centered: false,
        })
        .then((value) => {
          if (value === true) {
            this.$store.dispatch("note/deleteUserNote", slug);
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style></style>
