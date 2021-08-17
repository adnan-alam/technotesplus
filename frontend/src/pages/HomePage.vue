<template>
  <div class="container">
    <b-row>
      <b-col cols="4" class="text-center my-4 mx-auto">
        <h1>Tech Notes Plus</h1>
      </b-col>
    </b-row>
    <b-row v-if="!loggedIn">
      <b-col cols="4" class="text-center my-4 mx-auto">
        To use this app you'll need to
        <router-link to="/login">
          Login
        </router-link>
        or
        <router-link to="/register">
          Register
        </router-link>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters("auth", ["loggedIn"]),
  },
};
</script>
