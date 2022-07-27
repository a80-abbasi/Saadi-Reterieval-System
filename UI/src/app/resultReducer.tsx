import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { RootState } from "./store";

export interface ResultState {
  result: any;
  modalData: any;
  isOpen: boolean;
}

const initialState: ResultState = {
  result: [],
  modalData: [],
  isOpen: false,
};

export const resultSlice = createSlice({
  name: "result",
  initialState,
  // The `reducers` field lets us define reducers and generate associated actions
  reducers: {
    setResult: (state, action) => {
      state.result = action.payload;
    },
    setModalData: (state, action) => {
      state.modalData = action.payload;
    },
    setIsOpen: (state, action) => {
      state.isOpen = action.payload;
    },
  },
});

export const { setResult, setModalData, setIsOpen } = resultSlice.actions;
export const selectResult = (state: RootState) => state.result;

export default resultSlice.reducer;
