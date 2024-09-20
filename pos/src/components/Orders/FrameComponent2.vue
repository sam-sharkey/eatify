<template>
  <div
    class="flex-1 flex flex-col items-start justify-start p-[18px] box-border relative gap-[15px] max-w-full text-center text-base text-white font-poppins"
  >
    <div
      class="w-full h-full absolute !m-[0] top-[0px] right-[0px] bottom-[0px] left-[0px] rounded-3xs bg-darkslategray-300"
    />
    <div
      class="self-stretch flex flex-col items-start justify-start gap-[15px] text-6xl text-darkslategray-200"
    >
      <div
        class="self-stretch flex flex-row items-start justify-start gap-2.5 mq450:flex-wrap"
      >
        <div
          class="flex flex-row items-start justify-start py-[11px] pl-[18px] pr-[17px] relative z-[1]"
        >
          <div
            class="h-full w-full absolute !m-[0] top-[0px] right-[0px] bottom-[0px] left-[0px] rounded-8xs bg-green-300"
          />
          <div
            class="flex-1 relative font-medium z-[1] mq450:text-xl"
            :style="separatorStyle"
          >
            {{ separator }}
          </div>
        </div>
        <div
          class="flex-1 flex flex-col items-start justify-start pt-1 px-0 pb-0 text-left text-base text-white"
        >
          <div
            class="self-stretch flex flex-row items-start justify-start gap-11 mq450:gap-[22px]"
          >
            <div
              class="flex flex-col items-start justify-start pt-0.5 px-0 pb-0"
            >
              <div class="flex flex-col items-start justify-start gap-[5px]">
                <div
                  class="relative font-medium inline-block min-w-[116px] z-[1]"
                >
                  Watson Joyce
                </div>
                <a
                  class="[text-decoration:none] relative text-xs font-light text-[inherit] inline-block min-w-[74px] z-[1]"
                  :style="order990Style"
                  >Order # 990</a
                >
              </div>
            </div>
            <div
              class="flex-1 flex flex-col items-end justify-start gap-[5px] text-right text-xs text-darkslategray-200"
            >
              <div
                class="rounded-8xs bg-honeydew flex flex-row items-start justify-start py-[5px] pl-[7px] pr-1.5 gap-0.5 z-[1]"
                :style="orderTimeDetailsStyle"
              >
                <div
                  class="flex flex-col items-start justify-start pt-[3px] px-0 pb-0"
                >
                  <img
                    class="w-3 h-3 relative"
                    loading="lazy"
                    alt=""
                    src="/group-1000010348.svg"
                  />
                </div>
                <div
                  class="flex-1 relative font-light inline-block min-w-[39px]"
                  :style="readyStyle"
                >
                  {{ ready }}
                </div>
              </div>
              <div
                class="self-stretch flex flex-row items-end justify-start gap-[3px] text-white"
              >
                <div
                  class="flex-1 flex flex-row items-start justify-start gap-[5px] z-[1]"
                  :style="frameDiv1Style"
                >
                  <div
                    class="flex flex-col items-start justify-start pt-1.5 px-0 pb-0"
                  >
                    <div
                      class="w-1.5 h-1.5 relative rounded-[50%] bg-limegreen"
                      :style="statusIndicatorStyle"
                    />
                  </div>
                  <div
                    class="flex-1 relative font-light"
                    :style="readyToServeStyle"
                  >
                    {{ readyToServe }}
                  </div>
                </div>
                <div
                  class="flex flex-col items-start justify-end pt-0 px-0 pb-[2.2px]"
                >
                  <img
                    class="w-[13px] h-[13px] relative z-[1]"
                    alt=""
                    src="/group-1171275328.svg"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div
        class="self-stretch flex flex-row items-start justify-between gap-5 text-left text-base text-white mq450:flex-wrap"
      >
        <div class="relative font-light z-[1]">Wednesday, 28, 2024</div>
        <div
          class="relative font-light text-right inline-block min-w-[70px] z-[1]"
        >
          4 : 48 PM
        </div>
      </div>
    </div>
    <img
      class="self-stretch relative max-w-full overflow-hidden max-h-full z-[1]"
      loading="lazy"
      alt=""
      :src="orderDivider"
    />
    <div
      class="self-stretch flex flex-row items-start justify-start gap-6 mq450:flex-wrap"
    >
      <div class="flex flex-col items-start justify-start gap-2.5">
        <div
          class="relative font-light text-gray-200 text-left inline-block min-w-[29px] z-[1]"
        >
          Qty
        </div>
        <div
          class="self-stretch flex flex-row items-start justify-start py-0 pl-[7px] pr-[5px]"
        >
          <div class="flex-1 relative font-light z-[1]">01</div>
        </div>
        <div
          class="self-stretch flex flex-row items-start justify-start py-0 pl-[7px] pr-[5px]"
        >
          <div class="flex-1 relative font-light z-[1]">01</div>
        </div>
        <div
          class="self-stretch flex flex-row items-start justify-start py-0 pl-1 pr-[3px]"
        >
          <div class="flex-1 relative font-light z-[1]">02</div>
        </div>
        <div
          class="self-stretch flex flex-row items-start justify-start py-0 pl-[7px] pr-[5px]"
        >
          <div class="flex-1 relative font-light z-[1]">01</div>
        </div>
      </div>
      <div
        class="flex-1 flex flex-col items-start justify-start py-0 pl-0 pr-[15px] gap-2.5 text-left"
      >
        <div class="relative font-light text-gray-200 z-[1]">Items</div>
        <div class="relative font-light z-[1]">Scrambled eggs with toast</div>
        <div class="relative font-light z-[1]">Smoked Salmon Bagel</div>
        <div class="relative font-light z-[1]">Belgian Wlfles</div>
        <div class="relative font-light z-[1]">Classi Lemoniade</div>
      </div>
      <div
        class="w-[39px] flex flex-col items-end justify-start gap-2.5 text-right"
      >
        <div class="w-10 relative font-light text-gray-200 inline-block z-[1]">
          Price
        </div>
        <div class="w-9 relative font-light inline-block z-[1]">$199</div>
        <div class="w-[35px] relative font-light inline-block z-[1]">$120</div>
        <div class="self-stretch relative font-light z-[1]">$220</div>
        <div class="w-[30px] relative font-light inline-block z-[1]">$110</div>
      </div>
    </div>
    <img
      class="self-stretch relative max-w-full overflow-hidden max-h-full z-[1]"
      loading="lazy"
      alt=""
      :src="itemDivider"
    />
    <div
      class="self-stretch h-[113px] flex flex-col items-start justify-start gap-[25px] text-left"
    >
      <div
        class="self-stretch flex flex-row items-start justify-between gap-5 mq450:flex-wrap"
      >
        <div class="relative font-light z-[1]">SubTotal</div>
        <div
          class="relative font-light text-right inline-block min-w-[41px] z-[1]"
        >
          $649
        </div>
      </div>
      <div
        class="self-stretch flex-1 flex flex-row items-start justify-start gap-2.5 text-center text-darkslategray-200 mq450:flex-wrap"
      >
        <div class="self-stretch flex flex-row items-start justify-start z-[1]">
          <div
            class="self-stretch flex-1 rounded-3xs border-green-300 border-[1px] border-solid flex flex-row items-center justify-center py-[18px] px-[26px]"
          >
            <img
              class="h-6 w-6 relative"
              loading="lazy"
              alt=""
              src="/group-1000010360.svg"
            />
          </div>
        </div>
        <div class="self-stretch flex flex-row items-start justify-start z-[1]">
          <div
            class="self-stretch flex-1 rounded-3xs border-green-300 border-[1px] border-solid flex flex-row items-center justify-center py-[18px] px-[26px]"
          >
            <img
              class="h-6 w-6 relative"
              loading="lazy"
              alt=""
              src="/group-1000010359.svg"
            />
          </div>
        </div>
        <div class="flex-1 flex flex-row items-start justify-start z-[1]">
          <div
            class="flex-1 rounded-3xs bg-green-300 flex flex-row items-start justify-start py-5 pl-[55px] pr-[54px]"
          >
            <div class="flex-1 relative font-medium">Pay Bill</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import type * as CSS from "csstype";

export default defineComponent({
  name: "FrameComponent2",
  props: {
    separator: { type: String },
    ready: { type: String },
    readyToServe: { type: String },
    orderDivider: { type: String },
    itemDivider: { type: String },
    groupIconDisplay: { type: String },
    groupIconMinWidth: { type: [Object, Array, String, Number, Boolean] },
    orderDetailsListTextDecoration: { type: String },
    quantityValueBackgroundColor: { type: String },
    itemsValueDisplay: { type: String },
    itemsValueMinWidth: { type: [Object, Array, String, Number, Boolean] },
    priceValuePadding: { type: [Object, Array, String, Number, Boolean] },
    totalHeaderBackgroundColor: { type: String },
    orderItemsTextDecoration: { type: String },
  },
  computed: {
    separatorStyle(): CSS.Properties {
      return {
        display: this.groupIconDisplay,
        minWidth: this.groupIconMinWidth,
      };
    },
    order990Style(): CSS.Properties {
      return {
        textDecoration: this.orderDetailsListTextDecoration,
      };
    },
    orderTimeDetailsStyle(): CSS.Properties {
      return {
        backgroundColor: this.quantityValueBackgroundColor,
      };
    },
    readyStyle(): CSS.Properties {
      return {
        display: this.itemsValueDisplay,
        minWidth: this.itemsValueMinWidth,
      };
    },
    frameDiv1Style(): CSS.Properties {
      return {
        padding: this.priceValuePadding,
      };
    },
    statusIndicatorStyle(): CSS.Properties {
      return {
        backgroundColor: this.totalHeaderBackgroundColor,
      };
    },
    readyToServeStyle(): CSS.Properties {
      return {
        textDecoration: this.orderItemsTextDecoration,
      };
    },
  },
});
</script>
