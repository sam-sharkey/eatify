<template>
  <div
    class="w-[1269px] h-[631px] relative max-w-full text-left text-sm text-white font-poppins"
  >
    <div
      class="absolute top-[0px] left-[25px] flex flex-col items-start justify-start max-w-full"
    >
      <div class="w-[1079px] h-[21px] relative max-w-full">
        <div
          class="absolute top-[0px] left-[31px] font-medium inline-block min-w-[55px]"
        >
          Product
        </div>
        <div
          class="absolute top-[0px] left-[166px] font-medium inline-block min-w-[102px]"
        >
          Product Name
        </div>
        <input
          class="m-0 absolute top-[6px] left-[0px] border-white border-[1px] border-solid box-border w-[11px] h-[11px]"
          type="checkbox"
        />
        <div
          class="absolute top-[0px] left-[889px] font-medium inline-block min-w-[35px]"
        >
          Price
        </div>
        <div
          class="absolute top-[0px] left-[1000px] font-medium inline-block min-w-[79px]"
        >
          Availability
        </div>
        <div
          class="absolute top-[0px] left-[493px] font-medium inline-block min-w-[50px]"
        >
          Item ID
        </div>
        <div
          class="absolute top-[0px] left-[633px] font-medium inline-block min-w-[39px]"
        >
          Stock
        </div>
        <div
          class="absolute top-[0px] left-[758px] font-medium text-right inline-block min-w-[67px]"
        >
          Category
        </div>
      </div>
    </div>
    <div
      class="absolute top-[31px] left-[0px] flex flex-col items-start justify-start max-w-full w-full"
    >
      <FrameComponent1 /><FrameComponent1
        propAlignSelf="stretch"
        propWidth="unset"
        propBackgroundColor="#3d4142"
      /><FrameComponent1
        propAlignSelf="stretch"
        propWidth="unset"
        propBackgroundColor="#292c2d"
      /><FrameComponent1
        propAlignSelf="stretch"
        propWidth="unset"
        propBackgroundColor="#3d4142"
      /><FrameComponent1
        propAlignSelf="stretch"
        propWidth="unset"
        propBackgroundColor="#292c2d"
      /><FrameComponent1
        propAlignSelf="unset"
        propWidth="1269px"
        propBackgroundColor="#3d4142"
      />
    </div>
  </div>
</template>
<script lang="ts">
  import { defineComponent } from "vue";
  import FrameComponent1 from "./FrameComponent1.vue";

  export default defineComponent({
    name: "ProductTable",
    components: { FrameComponent1 },
  });
</script>
