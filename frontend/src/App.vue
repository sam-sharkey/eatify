<template>
  <PageHeader />
  <HighlightsWidget />
  <MenuWidget />
  <PictureWidget />
  <NewsWidget />
  <!---nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav>
  <router-view /--->
  <PageFooter />
</template>

<script lang="ts">
import { defineComponent } from "vue";
//import { useDark } from "@vueuse/core";
import PageHeader from "./components/PageHeader.vue";
import MenuWidget from "./components/MenuWidget.vue";
import HighlightsWidget from "./components/HighlightsWidget.vue";
import PageFooter from "./components/PageFooter.vue";
import PictureWidget from "./components/PictureWidget.vue";
import NewsWidget from "./components/NewsWidget.vue";

export default defineComponent({
  components: {
    PageHeader,
    MenuWidget,
    HighlightsWidget,
    PageFooter,
    PictureWidget,
    NewsWidget,
  },
});
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
