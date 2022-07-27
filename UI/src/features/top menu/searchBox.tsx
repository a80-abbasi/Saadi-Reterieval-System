import * as React from "react";
import Paper from "@mui/material/Paper";
import InputBase from "@mui/material/InputBase";
import Divider from "@mui/material/Divider";
import IconButton from "@mui/material/IconButton";
import { Typography } from "@mui/material";

import MenuIcon from "@mui/icons-material/Menu";
import SearchIcon from "@mui/icons-material/Search";
import DirectionsIcon from "@mui/icons-material/Directions";
import { selectMenu, setSearch } from "../../app/menuReducer";
import { useAppDispatch, useAppSelector } from "../../app/hooks";
import { setResult } from "../../app/resultReducer";
import { clustringText, searchText } from "../../logic/controller";
import { AutoComplete } from "./autoComplete";

export function SearchBox() {
  const menu: any = useAppSelector(selectMenu);
  const dispatch = useAppDispatch();
  const search = async () => {
    let result;
    if (menu.cluster) {
      const data = await clustringText("search", menu.search);
      console.log("cluster search: ", menu.search, data["class"].slice(0, 10));
      result = data["class"].slice(0, 10);
    } else {
      if (menu.enginStatus === "page rank" || menu.enginStatus === "hits") return;
      const data = await searchText(menu.search , menu.enginStatus)
      console.log("normal search: ",menu.search ,menu.enginStatus, data)
      result = data.result
    }

    dispatch(setResult(result));
  };
  const handleChange = (value: string) => {
    dispatch(setSearch(value));
  };

  return (
    <Paper
      sx={{ p: "2px 4px", display: "flex", alignItems: "center", width: 505 }}
    >
      {/* <IconButton sx={{ p: "10px" }} aria-label="menu">
        <MenuIcon />
      </IconButton> */}
      <IconButton sx={{ p: "10px" }} onClick={search}>
        <SearchIcon />
      </IconButton>
      <Divider sx={{ height: 28, m: 0.5 }} orientation="vertical" />
      {/* <Typography> {menu.search} asdsdas</Typography> */}

      <AutoComplete value2={menu.search} onChange={handleChange} />
      {/* <InputBase
        
        
      /> */}

      <IconButton color="primary" sx={{ p: "10px" }} onClick={search}>
        <DirectionsIcon />
      </IconButton>
    </Paper>
  );
}
