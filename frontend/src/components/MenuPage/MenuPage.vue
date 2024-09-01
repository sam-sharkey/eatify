<template>
  <div
    class="w-full relative bg-oldlace flex flex-col items-start justify-start leading-[normal] tracking-[normal] text-left text-[0.994rem] text-gray-200 font-inter"
  >
    <RestaurantInfo />

    <MenuCategoriesHeader
      :categories="menuCategories"
      :activeCategory="activeCategory"
    />

    <main
      class="w-full flex flex-col items-start justify-start pt-[4rem] pb-[0rem] pl-[1.75rem] pr-[1rem] box-border gap-[4rem] mq450:gap-[1rem] mq800:gap-[2rem] mq1350:pt-[1.25rem] mq1350:box-border"
      @scroll="handleScroll"
    >
      <div
        v-for="category in menuCategories"
        :key="category"
        :data-category="category"
        class="menu-section w-full"
      >
        <component
          :is="
            category === 'Custom' ? 'CustomSaladsParent' : 'MenuListComponent'
          "
          :menuItemClassification="category"
        />
      </div>
    </main>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from "vue";
import RestaurantInfo from "./RestaurantInfo.vue";
import MenuListComponent from "./MenuListComponent.vue";
import CustomSaladsParent from "./CustomSaladsParent.vue";
import MenuCategoriesHeader from "./MenuCategoriesHeader.vue";

export default defineComponent({
  name: "OrderMenuPage",
  components: {
    RestaurantInfo,
    MenuListComponent,
    CustomSaladsParent,
    MenuCategoriesHeader,
  },
  setup() {
    const menuCategories = ref([
      "Featured",
      "High Protein",
      "Bowls",
      "Salads",
      "Custom",
      "Kid's Meals",
      "Sides",
      "Desserts",
      "Beverage",
    ]);

    const activeCategory = ref(menuCategories.value[0]);

    const handleScroll = () => {
      const sections = document.querySelectorAll(".menu-section");

      for (const section of sections) {
        const rect = section.getBoundingClientRect();
        if (rect.top <= 100 && rect.bottom >= 100) {
          activeCategory.value =
            section.getAttribute("data-category") || activeCategory.value;
          break;
        }
      }
    };

    onMounted(() => {
      document.addEventListener("scroll", handleScroll);
    });

    return {
      menuCategories,
      activeCategory,
      handleScroll,
    };
  },
});
</script>
