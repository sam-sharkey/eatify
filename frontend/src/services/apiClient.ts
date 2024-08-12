// apiClient.ts
import axios from "axios";
import { MenuItem as MenuItemType, Highlight } from "../components/types";

const apiClient = axios.create({
  baseURL: `${process.env.VUE_APP_BACKEND_URL}`, // Update this to your Django server URL
  headers: {
    "Content-Type": "application/json",
  },
});

// Function to get restaurant ID by name
export const getRestaurantIdByName = async (
  restaurantName: string
): Promise<number> => {
  try {
    const response = await apiClient.get(
      `/api/restaurants/?name=${encodeURIComponent(restaurantName)}`
    );
    if (response.data && response.data.length > 0) {
      return response.data[0].id; // Assuming the response contains the restaurant ID
    } else {
      throw new Error("Restaurant not found");
    }
  } catch (error) {
    console.error("Error fetching restaurant ID:", error);
    throw error;
  }
};

export const fetchMenuItems = async (): Promise<MenuItemType[]> => {
  try {
    const response = await apiClient.get<MenuItemType[]>("/api/menu-items/");
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
