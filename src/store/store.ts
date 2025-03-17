import { configureStore } from '@reduxjs/toolkit';
import presentationReducer from './presentationSlice';

// Configure the store
const store = configureStore({
  reducer: {
    presentation: presentationReducer,
  },
  middleware: (getDefaultMiddleware: (config: any) => any[]) => getDefaultMiddleware({
    serializableCheck: false, // Disable serializable check for non-serializable values
  }),
});

// Define RootState type
export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

export default store;
