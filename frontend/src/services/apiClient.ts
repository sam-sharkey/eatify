// apiClient.ts
import axios from "axios";
import {
  MenuItem as MenuItemType,
  Highlight,
  Restaurant,
  ItemOption,
} from "../components/types";

const apiClient = axios.create({
  baseURL: `${process.env.VUE_APP_BACKEND_URL}`, // Update this to your Django server URL
  headers: {
    "Content-Type": "application/json",
  },
});

// Function to get restaurant ID by name
export const getRestaurantByName = async (
  restaurantName: string
): Promise<Restaurant> => {
  try {
    const response = await apiClient.get(
      `/api/restaurants/?name=${encodeURIComponent(restaurantName)}`
    );
    if (response.data && response.data.length > 0) {
      return {
        id: response.data[0].id,
        logo_src: response.data[0].logo_src,
        name: response.data[0].name,
      }; // Assuming the response contains the restaurant ID
    } else {
      throw new Error("Restaurant not found");
    }
  } catch (error) {
    console.error("Error fetching restaurant ID:", error);
    throw error;
  }
};

export const fetchMenuItems = async (
  restaurantId: number
): Promise<MenuItemType[]> => {
  try {
    const response = await apiClient.get<MenuItemType[]>(
      `/api/menu-items/${restaurantId}/`
    );
    return response.data;
  } catch (error) {
    console.error("Failed to fetch menu items:", error);
    throw error;
  }
};

export const fetchItemOptions = async (
  restaurantId: number
): Promise<ItemOption[]> => {
  try {
    const response = await apiClient.get<ItemOption[]>(
      `/api/item-options/${restaurantId}/`
    );
    return response.data;
  } catch (error) {
    console.error("Failed to fetch menu items:", error);
    throw error;
  }
};

export const fetchHighlights = async (
  restaurantId: number
): Promise<Highlight[]> => {
  try {
    const response = await apiClient.get(`/api/highlights/${restaurantId}/`);
    return response.data;
  } catch (error) {
    console.error("Error fetching highlights:", error);
    throw error;
  }
};

// Function to fetch header configuration
export const fetchHeaderConfig = async (restaurantId: number) => {
  const response = await apiClient.get(`/api/header-config/${restaurantId}/`);
  return response.data;
};

// Function to fetch footer configuration
export const fetchFooterConfig = async (restaurantId: number) => {
  const response = await apiClient.get(`/api/footer-config/${restaurantId}/`);
  return response.data;
};

// Function to fetch main page configuration
export const fetchMainPageConfig = async (restaurantId: number) => {
  const response = await apiClient.get(
    `/api/main-page-config/${restaurantId}/`
  );
  return response.data;
};

// Function to fetch location data
export const fetchLocations = async (restaurantId: number) => {
  const response = await apiClient.get(`/api/locations/${restaurantId}/`);
  return response.data;
};
