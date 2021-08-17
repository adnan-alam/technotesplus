<template>
  <b-modal
    id="modal_add_note"
    size="lg"
    centered
    hide-footer
    :scrollable="true"
    no-enforce-focuse
    title="Add Note"
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

      this.$store.dispatch("note/addUserNote", formData).then((response) => {
        if (response.status == 201) {
          this.$bvModal.hide("modal_add_note");
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

    onShow() {
      this.setExistingTags(this.note.tagsList);
    },
    onHide() {
      this.existingTags = [];
      this.form.title = "";
      this.form.tags = [];
      this.form.content = "";
    },
  },
};
</script>

<style>
@import "https://cdn.jsdelivr.net/npm/@voerro/vue-tagsinput@2.7.1/dist/style.css";
</style>
