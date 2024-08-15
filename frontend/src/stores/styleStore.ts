// stores/styleStore.ts
import { defineStore } from "pinia";

export const useStyleStore = defineStore("style", {
  state: () => ({
    headerCss: "",
    highlightsCss: "",
    menuCss: "",
    featureCss: "",
    newsCss: "",
    footerCss: "",
  }),
  actions: {
    setHeaderCss(css: string) {
      this.headerCss = css;
    },
    setHighlightsCss(css: string) {
      this.highlightsCss = css;
    },
    setMenuCss(css: string) {
      this.menuCss = css;
    },
    setFeatureCss(css: string) {
      this.featureCss = css;
    },
    setNewsCss(css: string) {
      this.newsCss = css;
    },
    setFooterCss(css: string) {
      this.footerCss = css;
    },
  },
});
