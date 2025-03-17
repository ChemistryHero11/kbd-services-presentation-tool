import { Product } from '../types';

// Local product library
export const defaultProducts: Product[] = [
  { 
    id: '1', 
    name: 'Custom T-Shirts', 
    category: 'Apparel', 
    price: 15.99, 
    description: '100% cotton, various sizes',
    image: 'https://via.placeholder.com/150?text=T-Shirt'
  },
  { 
    id: '2', 
    name: 'Promo Pens', 
    category: 'Writing', 
    price: 0.89, 
    description: 'Ballpoint with logo printing',
    image: 'https://via.placeholder.com/150?text=Pen'
  },
  { 
    id: '3', 
    name: 'Logo Tote Bags', 
    category: 'Bags', 
    price: 4.99, 
    description: 'Reusable eco-friendly totes',
    image: 'https://via.placeholder.com/150?text=Tote'
  },
];
