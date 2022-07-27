import Box from "@mui/material/Box";
import { Stack, Typography } from "@mui/material";
import Paper from "@mui/material/Paper";
import Grid from "@mui/material/Grid";
import { PoetCluster } from "./poetCluster";
import { ClusterModal } from "./clusterModal";
import { useAppDispatch, useAppSelector } from "../../app/hooks";
import { selectResult, setIsOpen, setModalData } from "../../app/resultReducer";
export const ClusterGrid = () => {
  const { result }: any = useAppSelector(selectResult);

  const dispatch = useAppDispatch();
  console.log("shhet")
  return (
    <Stack sx={{ p: 1 }} alignItems="center">
      <Grid
        container
        spacing={1}
        direction="row"
        justifyContent="center"
        alignItems="center"
      >
        {result &&
          Object.keys(result).map((e) => {
            return (
              <Grid item spacing={2}>
                <PoetCluster
                  data={result[e]}
                  onClick={(data:any) => {
                    dispatch(setModalData(data));
                    dispatch(setIsOpen(true));
                  }}
                />
              </Grid>
            );
          })}
      </Grid>
    </Stack>
  );
};
