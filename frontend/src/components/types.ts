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
