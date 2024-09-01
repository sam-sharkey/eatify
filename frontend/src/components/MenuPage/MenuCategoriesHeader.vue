<template>
  <div
    class="sticky z-10 top-20 w-full bg-oldlace border-b-[1px] border-gray-300 border-solid box-border flex flex-row items-start justify-center py-[0rem] px-[1.25rem] max-w-full"
  >
    <div
      class="flex flex-row items-start justify-center max-w-full [row-gap:20px] mq1150:flex-wrap"
    >
      <div
        v-for="category in categories"
        :key="category"
        class="flex flex-row items-start justify-start cursor-pointer"
        @click="scrollToSection(category)"
      >
        <div class="flex flex-col py-2">
          <div
            :class="[
              'px-4',
              isCategoryActive(category)
                ? 'underline border-5 border-black'
                : '',
            ]"
          >
            {{ category }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "MenuCategoriesHeader",
  props: {
    categories: {
      type: Array as () => string[],
      required: true,
    },
    activeCategory: {
      type: String,
      required: true,
    },
  },
  setup(props) {
    const isCategoryActive = (category: string) => {
      return category === props.activeCategory;
    };

    const scrollToSection = (category: string) => {
      const sectionElement = document.querySelector(
        `[data-category="${category}"]`
      );
      if (sectionElement) {
        sectionElement.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    };

    return { isCategoryActive, scrollToSection };
  },
});
</script>
