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

export function SearchBox() {
  const menu = useAppSelector(selectMenu);
  const dispatch = useAppDispatch();
  const search = () => {
    let result = [
      {
        text: "با جوانی سر خوش است این پیر بی تدبیر را جهل باشد با جوانان پنجه کردن پیر را",
      },
      { text: "روز بازار جوانی پنج روزی بیش نیست نقد را باش اي پسر کآفت بود تأخیر را       " },
      {
        text: "اي که گفتی دیده از دیدار بت رویان بدوز هر چه گویی چاره دانم کرد جز تقدیر را",
      },
      {
        text: "زهد پیدا کفر پنهان بود چندین روزگار  پرده از سر برگرفتیم آن همه ی تزویر را",
      },
    ];
    dispatch(setResult(result));
  };
  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    dispatch(setSearch(event.target.value));
  };

  return (
    <Paper
      sx={{ p: "2px 4px", display: "flex", alignItems: "center", width: 455 }}
    >
      {/* <IconButton sx={{ p: "10px" }} aria-label="menu">
        <MenuIcon />
      </IconButton> */}
      <IconButton sx={{ p: "10px" }} onClick={search}>
        <SearchIcon />
      </IconButton>
      <Divider sx={{ height: 28, m: 0.5 }} orientation="vertical" />
      <InputBase
        sx={{
          ml: 1,
          flex: 1,
          "& input::placeholder": {
            fontFamily:"Lalezar-Regular"
          },
        }}
        placeholder={"جستجو کنید"}
        value={menu.search}
        onChange={handleChange}
      />

      <IconButton color="primary" sx={{ p: "10px" }} onClick={search}>
        <DirectionsIcon />
      </IconButton>
    </Paper>
  );
}
