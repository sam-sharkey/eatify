<template>
  <PageHeader
    :leftHeaderItems="headerConfig.leftHeaderItems"
    :rightHeaderItems="headerConfig.rightHeaderItems"
  />
  <HighlightsWidget v-if="mainPageConfig.highlightsVisible" />
  <MenuWidget v-if="mainPageConfig.menuVisible" />
  <FeatureWidget v-if="mainPageConfig.featureVisible" />
  <NewsWidget v-if="mainPageConfig.newsVisible" />
  <PageFooter
    v-if="
      footerConfig.linksVisible ||
      footerConfig.appDownloadVisible ||
      footerConfig.newsletterVisible
    "
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
import { useStyleStore } from "./stores/styleStore";

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
    const styleStore = useStyleStore();

    const headerConfig = ref({
      leftHeaderItems: [],
      rightHeaderItems: [],
    });

    const footerConfig = ref({
      linksVisible: false,
      appDownloadVisible: false,
      newsletterVisible: false,
    });

    const mainPageConfig = ref({
      highlightsVisible: false,
      menuVisible: false,
      featureVisible: false,
      newsVisible: false,
    });

    const fetchConfig = async () => {
      try {
        const headerData = await fetchHeaderConfig(restaurantId);
        headerConfig.value = {
          leftHeaderItems: headerData.left_header_items,
          rightHeaderItems: headerData.right_header_items,
        };
        styleStore.setHeaderCss(headerData.custom_css);

        const footerData = await fetchFooterConfig(restaurantId);
        footerConfig.value = {
          linksVisible: footerData.links_visible,
          appDownloadVisible: footerData.app_download_visible,
          newsletterVisible: footerData.newsletter_visible,
        };
        styleStore.setFooterCss(footerData.custom_css);

        const mainPageData = await fetchMainPageConfig(restaurantId);
        mainPageConfig.value = {
          highlightsVisible: mainPageData.highlights_visible,
          menuVisible: mainPageData.menu_visible,
          featureVisible: mainPageData.feature_visible,
          newsVisible: mainPageData.news_visible,
        };
        styleStore.setHighlightsCss(mainPageData.custom_css);
        styleStore.setMenuCss(mainPageData.custom_css);
        styleStore.setFeatureCss(mainPageData.custom_css);
        styleStore.setNewsCss(mainPageData.custom_css);
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
