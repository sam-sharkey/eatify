<template>
  <HighlightsWidget v-if="mainPageConfig.highlightsVisible" />
  <MenuWidget v-if="mainPageConfig.menuVisible" />
  <FeatureWidget v-if="mainPageConfig.featureVisible" />
  <NewsWidget v-if="mainPageConfig.newsVisible" />
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from "vue";
import { fetchMainPageConfig } from "../../services/apiClient";
import MenuWidget from "../Menu/MenuWidget.vue";
import HighlightsWidget from "../Highlights/HighlightsWidget.vue";
import FeatureWidget from "../Picture/FeatureWidget.vue";
import NewsWidget from "../News/NewsWidget.vue";
import { useRestaurantStore } from "../../stores/restaurant";

export default defineComponent({
  components: {
    MenuWidget,
    HighlightsWidget,
    FeatureWidget,
    NewsWidget,
  },
  setup() {
    const store = useRestaurantStore();

    const mainPageConfig = ref({
      highlightsVisible: false,
      menuVisible: false,
      featureVisible: false,
      newsVisible: false,
      cssVariables: {},
    });

    const fetchConfig = async () => {
      const restaurantId = store.getRestaurant.id; // Get the restaurant ID from the store
      if (restaurantId !== null) {
        try {
          const mainPageData = await fetchMainPageConfig(restaurantId);
          mainPageConfig.value = {
            highlightsVisible: mainPageData.highlights_visible,
            menuVisible: mainPageData.menu_visible,
            featureVisible: mainPageData.feature_visible,
            newsVisible: mainPageData.news_visible,
            cssVariables: mainPageData.css_variables,
          };
        } catch (error) {
          console.error("Failed to fetch configuration data:", error);
        }
      }
    };

    onMounted(fetchConfig);

    return { mainPageConfig };
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
