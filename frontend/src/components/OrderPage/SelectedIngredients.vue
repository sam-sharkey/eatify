<template>
  <div
    class="w-full flex flex-col items-start justify-start pt-0 px-8 pb-6 box-border gap-4 max-w-[1520px] shrink-0 text-center text-smi text-gray-100 font-inter"
  >
    <div
      class="self-stretch flex flex-row items-end justify-start flex-wrap content-end gap-[8.1px]"
    >
      <ListItem2
        background="/background.svg"
        springMix="Spring Mix"
        container="/container1@2x.png"
      /><ContainerComponent background="/background.svg" />
      <div
        class="h-[175px] w-[153.3px] flex flex-col items-start justify-center pt-1 px-2 pb-0 box-border text-sm-1"
      >
        <div
          class="self-stretch flex-1 flex flex-col items-start justify-start relative"
        >
          <img
            class="w-full h-full absolute !m-[0] top-[1.75%] right-[0px] bottom-[-1.75%] left-[0px] rounded-xl max-w-full overflow-hidden max-h-full"
            alt=""
            src="/background.svg"
          />
          <div
            class="self-stretch flex-1 rounded-2xl bg-honeydew flex flex-col items-center justify-start p-3 z-[1]"
          >
            <div
              class="w-[86px] flex flex-col items-start justify-center py-2 px-5 box-border"
            >
              <div
                class="w-full overflow-hidden flex flex-col items-center justify-start py-0 px-px box-border max-w-[46.42px]"
              >
                <a
                  class="[text-decoration:none] relative leading-[16px] text-[inherit] inline-block min-w-[43px]"
                  >Apples</a
                >
              </div>
            </div>
            <div
              class="self-stretch flex-1 flex flex-col items-center justify-center pt-0 px-[11px] pb-2 relative text-left text-xs text-white"
            >
              <img
                class="w-full flex-1 relative max-w-[113.33px] overflow-hidden max-h-full object-cover"
                alt=""
                src="/container-110@2x.png"
              />
              <div
                class="w-[calc(100%_+_12.3px)] !m-[0] absolute right-[-6.15px] bottom-[-6px] left-[-6.15px] flex flex-row items-start justify-between gap-0 [row-gap:20px] z-[1]"
              >
                <div
                  class="h-8 w-8 rounded-13xl bg-oldlace border-honeydew border-[2px] border-solid box-border flex flex-col items-center justify-center py-1 px-0.5"
                >
                  <img
                    class="w-6 h-6 relative"
                    alt=""
                    src="/button--remove-spring-mix--svg.svg"
                  />
                </div>
                <div
                  class="w-[93.3px] flex flex-col items-end justify-start min-w-[32px]"
                >
                  <div
                    class="w-8 rounded-13xl bg-darkslategray-200 border-honeydew border-[2px] border-solid box-border flex flex-col items-center justify-center py-[5px] px-[7px]"
                  >
                    <div
                      class="flex flex-col items-start justify-start py-0 px-1"
                    >
                      <div
                        class="relative leading-[16px] inline-block min-w-[6px]"
                      >
                        1
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
    <div
      class="self-stretch flex flex-row items-start justify-start py-0 px-2 box-border max-w-full text-sm-5"
    >
      <div
        class="flex-1 flex flex-row items-end justify-start gap-[8.1px] max-w-full mq450:flex-wrap"
      >
        <ContainerComponent1
          background="/background.svg"
          container="/container-25@2x.png"
        /><ListItem2
          background="/background.svg"
          vegSlaw="Veg Slaw"
          container="/container-310@2x.png"
        /><ContainerComponent2
          background="/background.svg"
          container="/container-44@2x.png"
        />
      </div>
    </div>
    <div
      class="self-stretch grid flex-row items-start justify-start pt-0 px-0 pb-1 gap-[0.1px] grid-cols-[repeat(3,_minmax(115px,_1fr))] mq450:justify-center mq450:grid-cols-[minmax(115px,_1fr)]"
    >
      <ListItem2
        springMixRemoveWidth="unset"
        background="/background.svg"
        springMix="Blue Cheese"
        propTextDecoration="unset"
        propMinWidth="78px"
        container="/container-51@2x.png"
      /><ListItem2
        propWidth="unset"
        background="/background.svg"
        propWidth1="unset"
        propPadding="0px 1px"
        vegSlaw="Hard Boiled Egg"
        propMinWidth="98px"
        container="/container-61@2x.png"
      /><ListItem2
        springMixRemoveWidth="unset"
        background="/background.svg"
        springMix="Parmesan Crisps"
        propTextDecoration="unset"
        propMinWidth="105px"
        container="/container-71@2x.png"
      />
    </div>
    <div
      class="w-[153.3px] flex flex-row items-start justify-start py-0 px-2 box-border text-sm"
    >
      <ContainerComponent3
        background="/background.svg"
        container="/container-81@2x.png"
      />
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import ListItem2 from "./ListItem2.vue";
import ContainerComponent from "./ContainerComponent.vue";
import ContainerComponent1 from "./ContainerComponent1.vue";
import ContainerComponent2 from "./ContainerComponent2.vue";
import ContainerComponent3 from "./ContainerComponent3.vue";

export default defineComponent({
  name: "SelectedIngredients",
  components: {
    ListItem2,
    ContainerComponent,
    ContainerComponent1,
    ContainerComponent2,
    ContainerComponent3,
  },
});
</script>
