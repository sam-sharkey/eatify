// apiClient.ts
import axios from "axios";
import {
  MenuItem as MenuItemType,
  Highlight,
  Restaurant,
  ItemOption,
  Order,
  Inventory,
  Staff,
} from "./types";

const apiClient = axios.create({
  baseURL: "http://localhost:8000", // Update this to your Django server URL
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
    console.error("Failed to fetch item options:", error);
    throw error;
  }
};

export const fetchInventory = async (
  restaurantId: number
): Promise<Inventory[]> => {
  try {
    const response = await apiClient.get<Inventory[]>(
      `/api/inventory/?restaurant_id=${restaurantId}`
    );
    return response.data;
  } catch (error) {
    console.error("Failed to fetch inventory:", error);
    throw error;
  }
};

export const updateInventory = async (
  inventory: Inventory
): Promise<Inventory[]> => {
  try {
    const response = await apiClient.put(
      `/api/inventory/${inventory.id}/`,
      inventory
    );
    return response.data;
  } catch (error) {
    console.error("Failed to fetch inventory:", error);
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

// Funciton to Place Order in Backend
export const placeOrder = async (restaurantId: number, orderData: Order) => {
  try {
    const response = await apiClient.post(
      `/api/orders/0/?restaurant_id=${restaurantId}`,
      orderData
    );
    console.log("Order placed successfully:", response.data);
    return response.data;
    // Optionally, you can redirect to a confirmation page or show a success message
  } catch (error) {
    console.error("Failed to place order:", error);
    return null;
  }
};

// Funciton to Get Order in Backend
export const getOrders = async (
  orderId: null | string,
  restaurantId: null | number
) => {
  let response;
  if (orderId) {
    response = await apiClient.get(`/api/orders/0/?order_id=${orderId}`);
  } else if (restaurantId) {
    response = await apiClient.get(
      `/api/orders/0/?restaurant_id=${restaurantId}`
    );
  }
  return response?.data;
};

// Funciton to Delete Order in Backend
export const deleteOrder = async (orderId: number) => {
  const response = await apiClient.delete(`/api/orders/${orderId}/`);
  return response.data;
};

// Funciton to Get Order in Backend
export const editOrder = async (orderId: number, editedOrder: Order) => {
  const response = await apiClient.put(`/api/orders/${orderId}/`, editedOrder);

  return response.data;
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

export const fetchStaff = async (): Promise<Staff[]> => {
  try {
    const response = await apiClient.get<Staff[]>("/api/staff/");
    return response.data;
  } catch (error) {
    console.error("Failed to fetch staff:", error);
    throw error;
  }
};

// Create a new staff member
export const createStaff = async (staff: Staff): Promise<Staff> => {
  try {
    const response = await apiClient.post<Staff>("/api/staff/", staff);
    return response.data;
  } catch (error) {
    console.error("Failed to create staff:", error);
    throw error;
  }
};

// Update an existing staff member
export const updateStaff = async (staff: Staff): Promise<Staff> => {
  try {
    const response = await apiClient.put<Staff>(
      `/api/staff/${staff.id}/`,
      staff
    );
    return response.data;
  } catch (error) {
    console.error("Failed to update staff:", error);
    throw error;
  }
};

// Delete a staff member
export const deleteStaff = async (staffId: string): Promise<void> => {
  try {
    await apiClient.delete(`/api/staff/${staffId}/`);
  } catch (error) {
    console.error("Failed to delete staff:", error);
    throw error;
  }
};
