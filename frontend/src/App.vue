<template>
  <div class="sticky top-0 z-50 bg-white">
    <PageHeader
      :leftHeaderItems="headerConfig.leftHeaderItems"
      :rightHeaderItems="headerConfig.rightHeaderItems"
    />
  </div>
  <router-view />
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
import { fetchHeaderConfig, fetchFooterConfig } from "./services/apiClient";
import PageFooter from "./components/Footer/PageFooter.vue";
import PageHeader from "./components/Header/PageHeader.vue";
import { useStyleStore } from "./stores/styleStore";
import { useRestaurantStore } from "./stores/restaurant";

export default defineComponent({
  components: {
    PageFooter,
    PageHeader,
  },
  setup() {
    const store = useRestaurantStore();
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

    const fetchConfig = async () => {
      const restaurantId = store.getRestaurant.id; // Get the restaurant ID from the store
      if (restaurantId !== null) {
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
        } catch (error) {
          console.error("Failed to fetch configuration data:", error);
        }
      }
    };

    onMounted(fetchConfig);

    return { headerConfig, footerConfig };
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
