export interface MenuItem {
  classification: string;
  name: string;
  image_src: string;
  description: string;
  tag: string;
  price: number;
  calories: number;
  options: ItemOption[];
}

// Define the OrderItem type (intermediate relation with quantity)
export interface OrderItem {
  item_option: ItemOption;
  quantity: number;
}

export interface Order {
  id?: number;
  item_options: OrderItem[]; // Array of selected ItemOptions
  delivery_type: string; // Can only be 'pickup' or 'delivery'
  store_location: string; // The store location address
  user_address: string; // The user's address for delivery
  total_cost: number; // The total cost of the order
  order_time: string; // ISO string representing the time of the order
  status?: string;
}

export interface ItemOption {
  id: string;
  classification: string;
  name: string;
  image_src: string;
  cost: number;
  calories: number;
  is_in_stock: boolean;
}

export interface Inventory {
  id: string;
  item_option: ItemOption; // This is the ItemOption associated with the Inventory
  location: string;
  quantity: number;
  low_quantity_alert: number; // Threshold for low inventory alert
}

export interface HamburgerMenuItem {
  name: string;
  path: string;
}

export interface Restaurant {
  id: number;
  name: string;
  logo_src: string;
}

export interface Location {
  name: string;
  address: string;
  phone_number: string;
  opening_hours: string;
  image_src: string;
}

export interface Highlight {
  title: string;
  header: string;
  description1: string;
  description2: string;
  image_src: string; // Assuming URLs are returned for images
  tag: string;
}
