<template>
  <b-card class="mb-4">
    <b-card-header>Tags</b-card-header>
    <b-card-body>
      <b-row>
        <b-col cols="6">
          <ul class="list-unstyled mb-0">
            <li v-for="tag in tagsList1" :key="tag.id">
              <a
                class="badge bg-secondary text-decoration-none link-light"
                href="#!"
                >{{ tag.name }}</a
              >
            </li>
          </ul>
        </b-col>
        <b-col cols="6">
          <ul class="list-unstyled mb-0">
            <li v-for="tag in tagsList2" :key="tag.id">
              <a
                class="badge bg-secondary text-decoration-none link-light"
                href="#!"
                >{{ tag.name }}</a
              >
            </li>
          </ul>
        </b-col>
      </b-row>
    </b-card-body>
  </b-card>
</template>

<script>
import { mapState } from "vuex";

export default {
  data() {
    return {
      tagsList1: [],
      tagsList2: [],
    };
  },

  created() {
    this.fetchTagsList();
  },

  computed: {
    ...mapState(["note"]),
  },

  methods: {
    chunkArrayInGroups(arr, size) {
      let arrayChunks = [];
      for (let i = 0; i < arr.length; i += size) {
        arrayChunks.push(arr.slice(i, i + size));
      }
      return arrayChunks;
    },

    fetchTagsList() {
      this.$store.dispatch("note/fetchTagsList").then((response) => {
        if (response.status === 200) {
          let arrayChunks = this.chunkArrayInGroups(this.note.tagsList, 2);
          this.tagsList1 = arrayChunks[0];
          this.tagsList2 = arrayChunks[1];
        }
      });
    },
  },
};
</script>

<style></style>
