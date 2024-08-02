<template>
  <div
    class="w-[1440px] bg-tasman max-w-full flex flex-col items-start justify-start p-9 box-border leading-[normal] tracking-[normal]"
  >
    <section
      class="w-full flex flex-row items-start justify-start relative gap-9 max-w-[1440px] text-left text-base text-huntergreen font-roboto-regular-155 lg:flex-wrap lg:max-w-full gap-[18px] mq825:max-w-full mq450:max-w-full mq1425:max-w-full"
    >
      <div
        class="flex-1 flex flex-col items-start justify-start pt-0 px-0 pb-[20.8px] box-border min-w-[433px] max-w-full lg:flex-1 mq825:min-w-full"
      >
        <div
          class="self-stretch flex flex-row items-start justify-start max-w-full shrink-0"
        >
          <a
            class="[text-decoration:none] flex-1 relative leading-[16px] uppercase text-[inherit] inline-block max-w-full"
            >SWEETGREEN EXCLUSIVES
          </a>
        </div>
        <div
          class="self-stretch flex flex-col items-start justify-between min-h-[658px] shrink-0 text-46xl-4"
        >
          <div
            class="self-stretch flex flex-col items-start justify-start gap-[6.1px]"
          >
            <div class="self-stretch flex flex-col items-start justify-start">
              <div
                class="self-stretch relative leading-[59.5px] mq825:text-[52px] mq825:leading-[48px] mq450:text-[39px] mq450:leading-[36px]"
              >
                <p class="m-0">Dive into the fan</p>
                <p class="m-0">favorites</p>
              </div>
            </div>
            <div
              class="w-full flex flex-col items-start justify-start gap-[9.1px] max-w-[575px] text-4xl-4 mq825:max-w-full"
            >
              <div
                class="self-stretch flex flex-col items-start justify-start pt-0 px-0 pb-[0.9px] shrink-0"
              >
                <div
                  class="relative leading-[28.8px] mq450:text-lgi mq450:leading-[23px]"
                >
                  <p class="m-0">
                    Ordered often and always a hit, these popular picks are
                  </p>
                  <p class="m-0">true sweetgreen staples.</p>
                </div>
              </div>
              <div
                class="self-stretch flex flex-col items-start justify-start pt-0 px-0 pb-[0.9px] shrink-0 text-4xl-3"
              >
                <div
                  class="self-stretch relative leading-[28.8px] mq450:text-lgi mq450:leading-[23px]"
                >
                  <p class="m-0">
                    This collection includes the Harvest Bowl, Kale Caesar,
                  </p>
                  <p class="m-0">
                    Guacamole Greens, Chicken Pesto Parm, and Hot
                  </p>
                  <p class="m-0">Honey Chicken plate.</p>
                </div>
              </div>
            </div>
          </div>
          <GenericButton text="ORDER NOW" />
        </div>
      </div>
      <div
        class="flex-[0.991] flex flex-row items-start justify-start py-6 px-[3px] box-border min-w-[433px] max-w-full lg:flex-1 mq825:pt-5 mq825:pb-5 mq825:box-border mq825:min-w-full"
      >
        <img
          class="h-[646.5px] flex-1 rounded-xl max-w-[659px] overflow-hidden object-cover max-h-[659px] mq825:max-w-full"
          loading="lazy"
          alt=""
          src="/picture--home-page-new-moduleimagejpg@2x.png"
        />
      </div>
      <div
        class="h-8 w-8 !m-[0] absolute top-[-14px] right-[-4px] rounded-981xl bg-razzmatazz flex flex-row items-center justify-center pt-2 px-[7px] pb-1.5 box-border z-[1]"
      >
        <img
          class="h-[18px] w-[18px] relative object-cover"
          loading="lazy"
          alt=""
          src="/right-arrow@2x.png"
        />
      </div>
      <div
        class="h-8 w-8 !m-[0] absolute top-[-14.5px] right-[52px] rounded-981xl bg-razzmatazz flex flex-row items-center justify-center pt-2 px-[7px] pb-1.5 box-border z-[1]"
      >
        <img
          class="h-[18px] w-[18px] relative object-contain"
          loading="lazy"
          alt=""
          src="/right-arrow-11@2x.png"
        />
      </div>
    </section>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import GenericButton from "./GenericButton.vue";

export default defineComponent({
  name: "GenericArticle",
  components: { GenericButton },
});
</script>
