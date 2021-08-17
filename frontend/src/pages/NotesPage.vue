<template>
  <div class="container">
    <b-row>
      <b-col cols="8">
        <list-notes></list-notes>
      </b-col>

      <b-col cols="4">
        <list-tags></list-tags>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import ListNotes from "../components/notes/ListNotes.vue";
import ListTags from "../components/notes/ListTags.vue";

export default {
  components: {
    ListNotes,
    ListTags,
  },
};
</script>
