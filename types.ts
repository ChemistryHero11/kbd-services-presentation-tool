// Extracting shared types to break circular dependencies
import { PresentationState } from '../types';

// Define the RootState type without importing from store
export interface RootState {
  presentation: PresentationState;
}

// AppDispatch type will be defined in store.ts
export type AppDispatch = any; // This will be properly typed in store.ts
