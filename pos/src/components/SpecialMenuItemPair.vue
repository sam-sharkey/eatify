<template>
  <div
    class="h-[146px] flex-1 relative max-w-[152px] text-left text-base text-white font-poppins"
  >
    <div
      class="absolute h-full w-full top-[0%] right-[0%] bottom-[0%] left-[0%] rounded-3xs bg-darkslategray-300"
    />
    <div
      class="absolute bottom-[15px] left-[15px] w-[68px] h-12"
      :style="groupDivStyle"
    >
      <div
        class="absolute bottom-[0px] left-[0px] font-light inline-block min-w-[68px]"
        :style="itemsStyle"
      >
        {{items}}
      </div>
      <div
        class="absolute bottom-[24px] left-[0px] font-medium inline-block min-w-[40px]"
        :style="pizzaStyle"
      >
        {{pizza}}
      </div>
    </div>
    <img
      class="absolute top-[15px] right-[15px] w-10 h-10"
      loading="lazy"
      alt=""
      :src="group1000010171"
    />
  </div>
</template>
<script lang="ts">
  import { defineComponent } from "vue";
  import type * as CSS from "csstype";

  export default defineComponent({
    name: "SpecialMenuItemPair",
    props: {
      items: { type: String },
      pizza: { type: String },
      group1000010171: { type: String },
      propWidth: { type: [Object, Array, String, Number, Boolean] },
      propMinWidth: { type: [Object, Array, String, Number, Boolean] },
      propMinWidth1: { type: [Object, Array, String, Number, Boolean] },
    },
    computed: {
      groupDivStyle(): CSS.Properties {
        return {
          width: this.propWidth,
        };
      },
      itemsStyle(): CSS.Properties {
        return {
          minWidth: this.propMinWidth,
        };
      },
      pizzaStyle(): CSS.Properties {
        return {
          minWidth: this.propMinWidth1,
        };
      },
    },
  });
</script>
