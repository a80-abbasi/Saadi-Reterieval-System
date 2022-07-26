import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { RootState } from "./store";

export interface MenuState {
  search: string;
  cluster: boolean;
  clusterAnimation: boolean;
  enginStatus:
    | "tfidf"
    | "fasttext"
    | "boolean"
    | "transformer"
    | "elastic"
    | "classification"
    | "HITS"
    | "Page Rank";
}

const initialState: MenuState = {
  search: "",
  cluster: false,
  clusterAnimation: false,
  enginStatus: "tfidf",
};

export const menuSlice: any = createSlice({
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
