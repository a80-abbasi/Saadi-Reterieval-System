import * as React from "react";
import Container from "@mui/material/Box";
import Stack from "@mui/material/Stack";
import "./mainPage.css";
import { SearchBox } from "../top menu/searchBox";
import { ClusterCheckBox } from "../top menu/clusterCheckBoxx";
import { NormalOptions } from "../top menu/normalOptions";
import { PoetCluster } from "../poetComponent/poetCluster";
import { Help } from "../help";
import background from "../../bg.png";
import text from "../../text.png";
import { useAppDispatch, useAppSelector } from "../../app/hooks";
import { selectMenu } from "../../app/menuReducer";
import { selectResult } from "../../app/resultReducer";
import { ClusterGrid } from "../poetComponent/clusterGrid";
import { ClusterModal } from "../poetComponent/clusterModal";
export const MainPage = () => {
  const menu = useAppSelector(selectMenu);
  const resultState = useAppSelector(selectResult);
  // const [hideMenu, setHideMenu] = React.useState(false);

  return (
    <Container
      sx={{
        width: "100%",
        minHeight: "150vh",
        backgroundImage: `linear-gradient(to top,rgba(245, 90, 242, 0.42),rgba(117, 19, 93, 0.63)), url(${background})`,
      }}
    >
      <Stack spacing={2} sx={{ pt:2 }} alignItems="center">
        <img src={`${text}`} width="200" alt={"sda"} loading="lazy" />
        <Stack alignItems="center">
          <Stack
            direction="row"
            spacing={0.5}
            justifyContent="space-around"
            sx={{ width: 655 }}
          >
            <SearchBox />
            <ClusterCheckBox />
          </Stack>
          {menu.clusterAnimation ? null : (
            <div className={`Modal ${menu.cluster ? "close" : "open"}`}>
              <NormalOptions />
            </div>
          )}
        </Stack>
        {menu.clusterAnimation && resultState.result.length > 0  ? (
          <ClusterGrid />
        ) : resultState.result.length > 0 ? (
          <PoetCluster />
        ) : (
          <Help />
        )}
      </Stack>
      <ClusterModal/>

    </Container>
  );
};
