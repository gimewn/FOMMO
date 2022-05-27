<template>
  <div class='account-error-list'>
    <p v-for="(errors, field) in authError" :key="field">
      {{field}}
      <ul>
        <li v-for="(error, idx) in errors" :key='idx'>
          {{error}}
        </li>
      </ul>
    </p>
  </div>
</template>

<script>

export default {
  name:'AccountError',
  computed:{
    authError(){
      return this.$store.getters.authError
    }
  },
}
</script>

<style>

</style>