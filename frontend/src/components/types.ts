export interface MenuItem {
  classification: string;
  name: string;
  image_src: string;
  description: string;
}

export interface HamburgerMenuItem {
  name: string;
  path: string;
}

export interface Highlight {
  title: string;
  header: string;
  description1: string;
  description2: string;
  image_src: string; // Assuming URLs are returned for images
  tag: string;
}
