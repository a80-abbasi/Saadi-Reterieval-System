import { configureStore, ThunkAction, Action } from "@reduxjs/toolkit";
import menuReducer from "./menuReducer";
import resultReducer from "./resultReducer";

export const store = configureStore({
  reducer: {
    menu: menuReducer,
    result: resultReducer,
  },
});

export type AppDispatch = typeof store.dispatch;
export type RootState = ReturnType<typeof store.getState>;
export type AppThunk<ReturnType = void> = ThunkAction<
  ReturnType,
  RootState,
  unknown,
  Action<string>
>;
