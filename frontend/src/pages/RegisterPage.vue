<template>
  <div>
    <b-row>
      <b-col cols="4" class="text-center mx-auto">
        <div>
          <form-register></form-register>
        </div>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import FormRegister from "../components/account/FormRegister.vue";

export default {
  components: {
    FormRegister,
  },
};
</script>
