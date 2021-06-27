<template>
  <div id="main-wrapper">
    <div class="mou"></div>
    <router-view/>
  </div>
</template>

<script>

export default {
  name: "MainWrapper",
}
</script>

<style lang="scss">
.router-linki {
  display: flex;
  flex-wrap: nowrap;
  flex-direction: row;
  justify-content: right;
  margin-left: auto;
  margin-right: 0;

  &__link-to {
    top: 10px;
    padding: $padding;
    width: fit-content;
    border: solid 1px #aeaeae;
  }
}

#main-wrapper {
  width: 55vw;
  margin: 0 auto;
}
</style>