<template>
  <div
    class="w-[1840px] max-w-full flex flex-col items-center justify-start pt-8 px-16 pb-0 box-border gap-24 leading-[normal] tracking-[normal] article-menu"
  >
    <MenuNav :menuItems="['Salads', 'Warm Bowls', 'Sides']" />
    <section
      class="w-[1440px] flex flex-row items-start justify-start py-0 px-16 box-border gap-8 max-w-[1440px] shrink-0 text-left menu-section"
    >
      <MenuItem
        header="Kale Caesar"
        imageSrc="/picture--sg-web-image-salad-buffalo-chickenpng@2x.png"
        :descriptionLines="[
          'Roasted chicken, tomatoes, parmesan crisps, shaved',
          'parmesan, shredded kale, chopped romaine, lime',
          'squeeze, caesar',
        ]"
        buttonText="Order Now"
      />
      <MenuItem
        header="Guacamole Greens"
        imageSrc="/picture--sg-web-image-salad-buffalo-chickenpng1@2x.png"
        :descriptionLines="[
          'Roasted chicken, avocado, tomatoes, pickled onions,',
          'shredded cabbage, tortilla chips, spring mix, chopped',
          'romaine, lime squeeze, lime cilantro jalapeño vinaigrette',
        ]"
        buttonText="Order Now"
      />
      <MenuItem
        header="Buffalo Chicken"
        imageSrc="/picture--sg-web-image-salad-buffalo-chickenpng2@2x.png"
        :descriptionLines="[
          'Blackened chicken, pickled onions, tomatoes, raw',
          'carrots, cilantro, blue cheese, za’atar breadcrumbs,',
          'shredded kale, chopped romaine, sweetgreen hot sauce,',
          'caesar',
        ]"
        buttonText="Order Now"
      />
    </section>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import MenuNav from "./MenuNav.vue";
import MenuItem from "./MenuItem.vue";

export default defineComponent({
  name: "ArticleMenu",
  components: { MenuNav, MenuItem },
});
</script>

<style scoped>
.article-menu {
  background-color: var(--color-oldlace); /* Replacing bg-oldlace */
  font-size: 3rem; /* text-5xl */
  font-family: "Roboto", sans-serif; /* font-roboto-regular-1575 */
  color: var(--color-huntergreen); /* Replace text-huntergreen */
}

.menu-section {
  font-size: 3rem; /* text-5xl */
  font-family: "Roboto", sans-serif; /* font-roboto-regular-1575 */
  color: var(--color-huntergreen); /* Replace text-huntergreen */
}

@media (max-width: 1450px) {
  .menu-section {
    max-width: 100%;
  }
}
</style>
