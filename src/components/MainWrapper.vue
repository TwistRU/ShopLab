<template>
  <div id="main-wrapper">
    <keep-alive>
      <router-view/>
    </keep-alive>
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
  flex-direction: row-reverse;

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