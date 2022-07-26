import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { RootState } from "./store";

export interface MenuState {
  search: string;
  cluster: boolean;
  clusterAnimation: boolean;
  enginStatus: "opt1" | "opt2" | "opt3" | "opt4" | "opt5";
}

const initialState: MenuState = {
  search: "",
  cluster: false,
  clusterAnimation: false,
  enginStatus: "opt1",
};

export const menuSlice = createSlice({
  name: "menu",
  initialState,
  // The `reducers` field lets us define reducers and generate associated actions
  reducers: {
    setCluster: (state, action) => {
      state.cluster = action.payload;
    },
    setClusterAnimation: (state, action) => {
      state.clusterAnimation = action.payload;
    },

    setSearch: (state, action) => {
      state.search = action.payload;
    },
    setEngineStatus: (state, action) => {
      state.enginStatus = action.payload;
    },
  },
});

export const { setCluster, setEngineStatus, setSearch, setClusterAnimation } =
  menuSlice.actions;
export const selectMenu = (state: RootState) => state.menu;

export default menuSlice.reducer;
