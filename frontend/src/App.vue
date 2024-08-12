<template>
  <PageHeader
    :leftHeaderItems="headerConfig.leftHeaderItems"
    :rightHeaderItems="headerConfig.rightHeaderItems"
    :customCss="headerConfig.customCss"
  />
  <HighlightsWidget
    v-if="mainPageConfig.highlightsVisible"
    v-bind:style="mainPageConfig.customCss"
  />
  <MenuWidget
    v-if="mainPageConfig.menuVisible"
    v-bind:style="mainPageConfig.customCss"
  />
  <FeatureWidget
    v-if="mainPageConfig.featureVisible"
    v-bind:style="mainPageConfig.customCss"
  />
  <NewsWidget
    v-if="mainPageConfig.newsVisible"
    v-bind:style="mainPageConfig.customCss"
  />
  <PageFooter
    v-if="
      footerConfig.linksVisible ||
      footerConfig.appDownloadVisible ||
      footerConfig.newsletterVisible
    "
    v-bind:style="footerConfig.customCss"
    :linksVisible="footerConfig.linksVisible"
    :appDownloadVisible="footerConfig.appDownloadVisible"
    :newsletterVisible="footerConfig.newsletterVisible"
  />
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from "vue";
import {
  fetchHeaderConfig,
  fetchFooterConfig,
  fetchMainPageConfig,
} from "./services/apiClient";
import PageHeader from "./components/Header/PageHeader.vue";
import MenuWidget from "./components/Menu/MenuWidget.vue";
import HighlightsWidget from "./components/Highlights/HighlightsWidget.vue";
import PageFooter from "./components/Footer/PageFooter.vue";
import FeatureWidget from "./components/Picture/FeatureWidget.vue";
import NewsWidget from "./components/News/NewsWidget.vue";

export default defineComponent({
  components: {
    PageHeader,
    MenuWidget,
    HighlightsWidget,
    PageFooter,
    FeatureWidget,
    NewsWidget,
  },
  setup() {
    const restaurantId = 1; // Replace with the actual restaurant ID
    const headerConfig = ref({
      leftHeaderItems: [],
      rightHeaderItems: [],
      customCss: "",
    });

    const footerConfig = ref({
      linksVisible: false,
      appDownloadVisible: false,
      newsletterVisible: false,
      customCss: "",
    });

    const mainPageConfig = ref({
      highlightsVisible: false,
      menuVisible: false,
      featureVisible: false,
      newsVisible: false,
      customCss: "",
    });

    const fetchConfig = async () => {
      try {
        const headerData = await fetchHeaderConfig(restaurantId);
        headerConfig.value = {
          leftHeaderItems: headerData.left_header_items,
          rightHeaderItems: headerData.right_header_items,
          customCss: headerData.custom_css,
        };

        const footerData = await fetchFooterConfig(restaurantId);
        footerConfig.value = {
          linksVisible: footerData.links_visible,
          appDownloadVisible: footerData.app_download_visible,
          newsletterVisible: footerData.newsletter_visible,
          customCss: footerData.custom_css,
        };

        const mainPageData = await fetchMainPageConfig(restaurantId);
        mainPageConfig.value = {
          highlightsVisible: mainPageData.highlights_visible,
          menuVisible: mainPageData.menu_visible,
          featureVisible: mainPageData.feature_visible,
          newsVisible: mainPageData.news_visible,
          customCss: mainPageData.custom_css,
        };
      } catch (error) {
        console.error("Failed to fetch configuration data:", error);
      }
    };

    onMounted(fetchConfig);

    return { headerConfig, footerConfig, mainPageConfig };
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
