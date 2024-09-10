<template>
  <div
    class="h-[828px] bg-antiquewhite max-w-full flex flex-row items-start justify-start pt-0 px-0.5 pb-0 box-border min-h-[828px] leading-[normal] tracking-[normal] text-left text-8xl-9 text-gray-100 font-inter mq450:h-auto mq1050:pl-5 mq1050:pr-5 mq1050:box-border"
  >
    <div
      class="w-[525px] bg-oldlace border-gray-100 border-r-[1px] border-solid box-border flex flex-col items-start justify-start max-w-[525px] shrink-0 mq1050:hidden mq750:max-w-full"
    >
      <div
        class="self-stretch h-[894px] overflow-y-auto shrink-0 flex flex-col items-start justify-start pt-0 px-0 pb-[764px] box-border max-w-full lg:pb-[497px] lg:box-border mq450:h-auto mq750:pb-[323px] mq750:box-border"
      >
        <div
          class="self-stretch flex flex-col items-center justify-start shrink-0"
        >
          <div
            class="w-full bg-oldlace flex flex-col items-start justify-start pt-0 px-10 pb-6 box-border max-w-[1520px]"
          >
            <div
              class="self-stretch flex flex-col items-start justify-start pt-10 px-0 pb-0"
            >
              <div
                class="self-stretch flex flex-row items-center justify-between min-h-[36px] gap-5 mq450:flex-wrap"
              >
                <div
                  class="flex flex-col items-start justify-start py-0 pl-0 pr-3"
                >
                  <a
                    class="[text-decoration:none] relative tracking-[1px] leading-[36px] text-[inherit] mq450:text-3xl mq450:leading-[29px]"
                    >Create Your Own</a
                  >
                </div>
                <div
                  class="h-8 w-8 rounded-81xl flex flex-col items-center justify-center"
                >
                  <img
                    class="w-8 h-8 relative"
                    loading="lazy"
                    alt=""
                    src="/svg1.svg"
                  />
                </div>
              </div>
              <div
                class="self-stretch flex flex-col items-start justify-start pt-2 px-0 pb-0 text-[14.1px]"
              >
                <div class="self-stretch relative leading-[22px]">
                  $19.70 - 915 cal
                </div>
              </div>
            </div>
          </div>
        </div>
        <SelectedIngredients />
      </div>
      <div
        class="self-stretch flex flex-col items-center justify-start max-w-full text-center text-mini"
      >
        <div
          class="w-full bg-oldlace border-gray-100 border-t-[1px] border-solid box-border flex flex-row items-start justify-start pt-[15px] px-7 pb-4 max-w-[1520px]"
        >
          <div
            class="w-[456px] flex flex-col items-start justify-start py-0 px-0 box-border max-w-full"
          >
            <div
              class="flex flex-row items-start justify-start flex-wrap content-start py-0 pl-0 pr-0.5 box-border max-w-[103%] shrink-0"
            >
              <div
                class="flex flex-col items-start justify-start py-0 pl-3 pr-[11px]"
              >
                <div class="flex flex-col items-start justify-start">
                  <div
                    class="rounded-81xl border-gray-100 border-[1px] border-solid flex flex-row items-center justify-center py-[11px] px-[79px]"
                  >
                    <div class="flex flex-col items-center justify-start">
                      <div
                        class="relative leading-[22px] inline-block min-w-[50px]"
                      >
                        Cancel
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="flex flex-col items-start justify-start py-0 pl-3 pr-[11px] ml-[-2px] text-mini-5 text-white"
              >
                <div class="flex flex-col items-start justify-start">
                  <div
                    class="rounded-81xl bg-darkslategray-200 flex flex-row items-center justify-center py-[13px] px-[74px]"
                  >
                    <div
                      class="flex flex-col items-center justify-start py-0 px-px"
                    >
                      <div
                        class="relative leading-[22px] inline-block min-w-[60px]"
                      >
                        I'm done
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <OptionsMenu></OptionsMenu>>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import SelectedIngredients from "./SelectedIngredients.vue";
import OptionsMenu from "./OptionsMenu.vue";

export default defineComponent({
  name: "CustomOrder",
  components: {
    SelectedIngredients,
    OptionsMenu,
  },
  setup() {
    return {};
  },
});
</script>
