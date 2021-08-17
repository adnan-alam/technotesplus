<template>
  <div>
    <b-row>
      <b-col cols="4" class="text-center mx-auto">
        <div>
          <form-login></form-login>
        </div>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import FormLogin from "../components/account/FormLogin.vue";

export default {
  components: {
    FormLogin,
  },
};
</script>
