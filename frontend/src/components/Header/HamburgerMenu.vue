<template>
  <div>
    <template v-if="showHamburger">
      <button @click="toggleMenu" class="hamburger-button">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-8 w-8 text-wwwsweetgreencom-bitter"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          stroke-width="2"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M4 6h16M4 12h16m-7 6h7"
          />
        </svg>
      </button>
    </template>
    <template v-else>
      <div class="menu-container open">
        <div class="p-4 border-b border-gray-200">
          <p class="font-bold text-lg cursor-pointer" @click="toggleMenu">
            Menu
          </p>
        </div>
        <div class="flex-grow overflow-y-auto">
          <ul class="p-4">
            <li v-for="item in menuItems" :key="item.name" class="mb-2">
              <router-link
                :to="item.path"
                class="block p-2 rounded"
                @click="toggleMenu"
              >
                {{ item.name }}
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </template>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType, ref } from "vue";

interface MenuItem {
  name: string;
  path: string;
}

export default defineComponent({
  name: "HamburgerMenu",
  props: {
    menuItems: {
      type: Array as PropType<MenuItem[]>,
      required: true,
    },
  },
  setup() {
    const showHamburger = ref(true);

    const toggleMenu = () => {
      showHamburger.value = !showHamburger.value;
    };

    return {
      showHamburger,
      toggleMenu,
    };
  },
});
</script>

<style scoped>
.hamburger-button {
  background: none;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.hamburger-button:focus {
  outline: none;
}

.menu-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 30%;
  height: 100%;
  background-color: var(--color-springwood);
  z-index: 50;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
  transition: transform 0.3s ease-in-out;
  transform: translateX(-100%);
}

.menu-container.open {
  transform: translateX(0);
}
</style>
