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
import {
  fetchHeaderConfig,
  fetchFooterConfig,
  fetchMainPageConfig,
} from "./services/apiClient";
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

    const mainPageConfig = ref({
      highlightsVisible: false,
      menuVisible: false,
      featureVisible: false,
      newsVisible: false,
      cssVariables: {},
    });

    type ColorObject = { r: number; g: number; b: number; a: number };

    const pSBC = (
      p: number,
      c0: string,
      c1?: string | null,
      l?: boolean
    ): string | null => {
      const i = parseInt;
      const m = Math.round;
      const a = typeof c1 === "string";

      const pSBCr = (d: string): ColorObject | null => {
        let n = d.length;
        let x: ColorObject = { r: 0, g: 0, b: 0, a: -1 };

        if (n > 9) {
          let [r, g, b, a] = d.split(",");
          n = d.length;
          if (n < 3 || n > 4) return null;
          x.r = i(r[3] === "a" ? r.slice(5) : r.slice(4));
          x.g = i(g);
          x.b = i(b);
          x.a = a ? parseFloat(a) : -1;
        } else {
          if (n === 8 || n === 6 || n < 4) return null;
          if (n < 6)
            d =
              "#" +
              d[1] +
              d[1] +
              d[2] +
              d[2] +
              d[3] +
              d[3] +
              (n > 4 ? d[4] + d[4] : "");
          let d_int = i(d.slice(1), 16);
          if (n === 9 || n === 5) {
            x.r = (d_int >> 24) & 255;
            x.g = (d_int >> 16) & 255;
            x.b = (d_int >> 8) & 255;
            x.a = m((d_int & 255) / 0.255) / 1000;
          } else {
            x.r = d_int >> 16;
            x.g = (d_int >> 8) & 255;
            x.b = d_int & 255;
            x.a = -1;
          }
        }
        return x;
      };

      if (
        typeof p !== "number" ||
        p < -1 ||
        p > 1 ||
        typeof c0 !== "string" ||
        (c0[0] !== "r" && c0[0] !== "#") ||
        (c1 && !a)
      )
        return null;

      const h = c0.length > 9;
      const f = pSBCr(c0);
      const t =
        c1 && c1 !== "c"
          ? pSBCr(c1)
          : p < 0
          ? { r: 0, g: 0, b: 0, a: -1 }
          : { r: 255, g: 255, b: 255, a: -1 };

      if (!f || !t) return null;

      const P = p < 0 ? -p : p;
      const P1 = 1 - P;

      let r, g, b, aFinal;

      if (l) {
        r = m(P1 * f.r + P * t.r);
        g = m(P1 * f.g + P * t.g);
        b = m(P1 * f.b + P * t.b);
      } else {
        r = m(Math.sqrt(P1 * f.r ** 2 + P * t.r ** 2));
        g = m(Math.sqrt(P1 * f.g ** 2 + P * t.g ** 2));
        b = m(Math.sqrt(P1 * f.b ** 2 + P * t.b ** 2));
      }

      const alpha = f.a >= 0 || t.a >= 0;
      aFinal = alpha ? (f.a < 0 ? t.a : t.a < 0 ? f.a : f.a * P1 + t.a * P) : 0;

      if (h) {
        return `rgb${alpha ? "a" : ""}(${r},${g},${b}${
          alpha ? "," + m(aFinal * 1000) / 1000 : ""
        })`;
      } else {
        return (
          "#" +
          (
            4294967296 +
            r * 16777216 +
            g * 65536 +
            b * 256 +
            (alpha ? m(aFinal * 255) : 0)
          )
            .toString(16)
            .slice(1, alpha ? undefined : -2)
        );
      }
    };

    const setCssVariables = (variables: Record<string, string>) => {
      const root = document.documentElement;
      for (const [key, value] of Object.entries(variables)) {
        // Set the 500 color (original color)
        root.style.setProperty(`${key}`, value);

        // Calculate intermediate colors (200, 300, 400, 600, 700, 800)
        for (let i = 100; i <= 900; i += 100) {
          const factor = ((500 - i) / 1000) * 1.5;
          const intermediateColor = pSBC(factor, value); // Adjusting factor range
          console.log(`${key}-${i}`);
          console.log(intermediateColor);
          root.style.setProperty(`${key}-${i}`, intermediateColor);
        }
      }
    };

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

          const mainPageData = await fetchMainPageConfig(restaurantId);
          mainPageConfig.value = {
            highlightsVisible: mainPageData.highlights_visible,
            menuVisible: mainPageData.menu_visible,
            featureVisible: mainPageData.feature_visible,
            newsVisible: mainPageData.news_visible,
            cssVariables: mainPageData.css_variables,
          };
          styleStore.setHighlightsCss(mainPageData.custom_css);
          styleStore.setMenuCss(mainPageData.custom_css);
          styleStore.setFeatureCss(mainPageData.custom_css);
          styleStore.setNewsCss(mainPageData.custom_css);
          // Apply global CSS variables
          console.log(mainPageData.css_variables);
          styleStore.setGlobalCss(mainPageData.css_variables);
          setCssVariables(mainPageData.css_variables);
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
