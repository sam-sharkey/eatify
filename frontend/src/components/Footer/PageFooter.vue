<template>
  <div
    class="max-w-full overflow-hidden flex flex-col items-start justify-start leading-[normal] tracking-[normal]"
  >
    <section
      class="self-stretch bg-oldlace overflow-hidden flex flex-row items-start justify-start max-w-full [row-gap:20px] mq1150:flex-wrap"
    >
      <FooterNewsletter /><FooterAppDownload />
    </section>
    <FooterLinks />
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import FooterNewsletter from "./FooterNewsletter.vue";
import FooterAppDownload from "./FooterAppDownload.vue";
import FooterLinks from "./FooterLinks.vue";

export default defineComponent({
  name: "PageFooter",
  components: { FooterNewsletter, FooterAppDownload, FooterLinks },
});
</script>
