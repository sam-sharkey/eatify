<template>
  <PageHeader />
  <ArticleHighlightsHighlight />
  <ArticleMenu />
  <GenericArticle />
  <NewsArticle />
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
import ArticleMenu from "./components/ArticleMenu.vue";
import ArticleHighlightsHighlight from "./components/ArticleHighlightsHighlight.vue";
import PageFooter from "./components/PageFooter.vue";
import GenericArticle from "./components/GenericArticle.vue";
import NewsArticle from "./components/NewsArticle.vue";

export default defineComponent({
  components: {
    PageHeader,
    ArticleMenu,
    ArticleHighlightsHighlight,
    PageFooter,
    GenericArticle,
    NewsArticle,
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
