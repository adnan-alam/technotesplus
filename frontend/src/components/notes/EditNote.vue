<template>
  <b-modal
    id="modal_edit_note"
    size="lg"
    centered
    hide-footer
    :scrollable="true"
    no-enforce-focuse
    title="Edit Note"
    @show="onShow"
    @hide="onHide"
  >
    <b-row class="my-4">
      <b-col cols="12">
        <b-form-group>
          <b-form-input
            v-model="form.title"
            type="text"
            placeholder="Title"
            required
          ></b-form-input>
        </b-form-group>
      </b-col>
    </b-row>

    <b-row class="my-4">
      <b-col cols="12">
        <ckeditor v-model="form.content"></ckeditor>
      </b-col>
    </b-row>

    <b-row class="my-4">
      <b-col cols="12">
        <tags-input
          element-id="tags"
          v-model="form.tags"
          :existing-tags="existingTags"
          :typeahead="true"
        />
      </b-col>
    </b-row>

    <b-row class="my-4">
      <b-col cols="12">
        <b-button variant="primary" @click="onSubmit">Submit</b-button>
      </b-col>
    </b-row>
  </b-modal>
</template>

<script>
import { mapState } from "vuex";
import VoerroTagsInput from "@voerro/vue-tagsinput";

export default {
  components: {
    "tags-input": VoerroTagsInput,
  },

  data() {
    return {
      existingTags: [],
      form: {
        title: "",
        content: "",
        tags: [],
      },
    };
  },

  computed: {
    ...mapState(["note"]),
  },

  methods: {
    onSubmit() {
      let tagsArray = [];

      let formData = JSON.parse(JSON.stringify(this.form));
      formData.tags.filter((obj) => {
        tagsArray.push(obj.value);
      });
      formData["tags"] = tagsArray;

      this.$store
        .dispatch("note/editUserNote", {
          noteSlug: this.note.selectedNote.slug,
          note: formData,
        })
        .then((response) => {
          if (response.status == 200) {
            this.$bvModal.hide("modal_edit_note");
          }
        });
    },

    setExistingTags(tagsList) {
      tagsList.forEach((obj) => {
        this.existingTags.push({
          key: obj.id,
          value: obj.name,
        });
      });
    },

    getFormTagsArray(formTags) {
      let tagsArray = [];
      this.existingTags.forEach((obj) => {
        if (formTags.includes(obj.value)) {
          tagsArray.push({
            key: obj.key,
            value: obj.value,
          });
        }
      });
      return tagsArray;
    },

    onShow() {
      this.setExistingTags(this.note.tagsList);
      let tagsArray = this.getFormTagsArray(this.note.selectedNote.tags);
      this.form.title = this.note.selectedNote.title;
      this.form.content = this.note.selectedNote.content;
      this.form.tags = tagsArray;
    },

    onHide() {
      this.existingTags = [];
      this.form.title = "";
      this.form.tags = [];
    },
  },
};
</script>

<style>
@import "https://cdn.jsdelivr.net/npm/@voerro/vue-tagsinput@2.7.1/dist/style.css";
</style>
