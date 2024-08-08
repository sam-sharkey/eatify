<template>
  <div
    class="w-[1958px] max-w-full flex flex-col items-center justify-start py-0 px-5 box-border leading-[normal] tracking-[normal] text-left text-[23.6px] text-huntergreen font-roboto-regular-155"
  >
    <div
      class="w-[1558px] flex flex-row items-baseline justify-between gap-5 max-w-full mq450:flex-wrap"
    >
      <a
        class="[text-decoration:none] relative leading-[29px] uppercase text-[inherit] mq450:text-lgi mq450:leading-[23px]"
        >The Latest</a
      >
      <div class="flex flex-col items-start justify-start text-base">
        <a
          class="[text-decoration:none] relative leading-[16px] uppercase text-[inherit] inline-block min-w-[108px]"
          >Read more →</a
        >
      </div>
    </div>
    <section
      class="flex flex-row flex-wrap items-start justify-center pt-0 px-[59px] pb-[13px] box-border gap-[13px] max-w-full text-left text-base text-huntergreen font-roboto-regular-155 lg:pl-[29px] lg:pr-[29px] lg:box-border"
    >
      <div
        class="rounded-xl bg-starkwhite flex flex-row items-start justify-center py-5 px-4 box-border gap-6 min-h-[220px] max-w-full mq750:flex-wrap"
      >
        <div
          class="w-[235.3px] flex flex-col items-start justify-between min-w-[235.3px] min-h-[180px] mq750:flex-1"
        >
          <div
            class="self-stretch flex flex-col items-start justify-start pt-0 px-0 pb-5 gap-[5px]"
          >
            <div class="self-stretch flex flex-col items-start justify-start">
              <div class="self-stretch relative leading-[20px] uppercase">
                Good Morning America
              </div>
            </div>
            <div
              class="self-stretch flex flex-col items-start justify-start font-georgia-regular-16"
            >
              <div class="self-stretch relative leading-[20px]">
                <p class="m-0">Naomi Osaka joins sweetgreen</p>
                <p class="m-0">as youngest investor</p>
              </div>
            </div>
          </div>
          <div
            class="self-stretch flex flex-col items-start justify-start text-base-5"
          >
            <div class="self-stretch relative leading-[20px]">
              <p class="m-0">Discover what our collab means</p>
              <p class="m-0">for the future of fast food…</p>
              <p class="m-0">Read more →</p>
            </div>
          </div>
        </div>
        <img
          class="h-[180px] w-[180px] relative rounded-xl overflow-hidden shrink-0 object-cover max-w-[180px] min-h-[180px] mq750:w-full"
          loading="lazy"
          alt=""
          src="/figure--inthenews01v3png@2x.png"
        />
      </div>
      <NewsLink
        source="NEW YORK TIMES"
        caption="In a burger world, can sweetgreen scale up?"
        diveIntoAJuicyPocastWithO="Learn how we're using tech to innovate fast-casual dining…"
        figureInTheNews01V3png="/figure--inthenews01v3png1@2x.png"
      /><NewsLink
        source="NPR HOW I BUILT THIS"
        caption="sweetgreen: Nicolas Jammet & Jonathan Neman"
        diveIntoAJuicyPocastWithO="Dive into a juicy pocast with our visionary founders…"
        figureInTheNews01V3png="/figure--inthenews01v3png2@2x.png"
      />
    </section>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import NewsLink from "./NewsLink.vue";

export default defineComponent({
  name: "NewsWidget",
  components: { NewsLink },
});
</script>
