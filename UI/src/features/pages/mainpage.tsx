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
import { selectResult, setIsOpen, setModalData } from "../../app/resultReducer";
import { ClusterGrid } from "../poetComponent/clusterGrid";
import { ClusterModal } from "../poetComponent/clusterModal";
import { LinkAnalysis } from "../top menu/link";
import { Typography } from "@mui/material";
export const MainPage = () => {
  const menu: any = useAppSelector(selectMenu);
  const resultState = useAppSelector(selectResult);
  const dispatch = useAppDispatch();
  // const [hideMenu, setHideMenu] = React.useState(false);

  return (
    <Container
      sx={{
        width: "100%",
        minHeight: "150vh",
        backgroundImage: `linear-gradient(to top,rgba(245, 90, 242, 0.42),rgba(117, 19, 93, 0.63)), url(${background})`,
      }}
    >
      <Stack spacing={2} sx={{ pt: 2 }} alignItems="center">
        <img src={`${text}`} width="200" alt={"sda"} loading="lazy" />
        <Stack alignItems="center">
          <Stack
            direction="row"
            spacing={0.5}
            justifyContent="space-around"
            sx={{ width: 735 }}
          >
            <SearchBox />
            <ClusterCheckBox />
          </Stack>
          {menu.clusterAnimation ? null : (
            <div className={`Modal ${menu.cluster ? "close" : "open"}`}>
              <Stack>
                <NormalOptions />
                <LinkAnalysis />
              </Stack>
            </div>
          )}
        </Stack>
         {/* <Typography> {Object.keys(resultState.result).length} </Typography> */}
        {/* <Typography> {JSON.stringify(resultState.result)} </Typography>  */}

        {menu.clusterAnimation &&
        !(resultState.result instanceof Array) &&
        Object.keys(resultState.result).length > 1 ? (
          <ClusterGrid />
        ) : menu.clusterAnimation && resultState.result instanceof Array ? (
          <PoetCluster
            data={resultState.result}
            onClick={(data: any) => {
              dispatch(setModalData(data));
              dispatch(setIsOpen(true));
            }}
          />
        ) : !menu.clusterAnimation && resultState.result instanceof Array && resultState.result.length> 0 ? (
          <PoetCluster
            data={resultState.result}
            onClick={(data: any) => {
              dispatch(setModalData(data));
              dispatch(setIsOpen(true));
            }}
          />
        ) : (
          <Help />
        )}
      </Stack>
      <ClusterModal />
    </Container>
  );
};
