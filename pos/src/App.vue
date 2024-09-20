<template>
  <div class="flex flex-col-2 bg-gray">
    <SidebarNavigation />
    <router-view />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import SidebarNavigation from "./components/Common/SidebarNavigation.vue";

export default defineComponent({
  name: "App",
  components: { SidebarNavigation },
});
</script>
