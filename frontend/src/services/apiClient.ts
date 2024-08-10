// apiClient.ts
import axios from "axios";
import { MenuItem as MenuItemType, Highlight } from "../components/types";

const apiClient = axios.create({
  baseURL: "http://localhost:8000", // Update this to your Django server URL
  headers: {
    "Content-Type": "application/json",
  },
});

export const fetchMenuItems = async (): Promise<MenuItemType[]> => {
  try {
    const response = await apiClient.get<MenuItemType[]>("/api/menu-items/");
    return response.data;
  } catch (error) {
    console.error("Failed to fetch menu items:", error);
    throw error;
  }
};

export const fetchHighlights = async (): Promise<Highlight[]> => {
  try {
    const response = await apiClient.get<Highlight[]>("/api/highlights/");
    return response.data;
  } catch (error) {
    console.error("Failed to fetch highlight data:", error);
    throw error;
  }
};
