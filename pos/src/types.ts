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
  selectedItems: OrderItem[]; // Array of selected ItemOptions
  deliveryType: string; // Can only be 'pickup' or 'delivery'
  storeLocation: string; // The store location address
  userAddress: string; // The user's address for delivery
  totalCost: number; // The total cost of the order
  orderTime: string; // ISO string representing the time of the order
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
