import Box from "@mui/material/Box";
import { Stack } from "@mui/material";
import Paper from "@mui/material/Paper";
import Grid from "@mui/material/Grid";
import { PoetCluster } from "./poetCluster";
import { ClusterModal } from "./clusterModal";
import { useAppDispatch } from "../../app/hooks";
import { setIsOpen, setModalData } from "../../app/resultReducer";
export const ClusterGrid = () => {
  const ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  const dispatch = useAppDispatch();

  return (
    <Stack sx={{ p: 1 }} alignItems="center">
      <Grid
        container
        spacing={1}
        direction="row"
        justifyContent="center"
        alignItems="center"
      >
        {ls.map((e) => {
          return (
            <Grid item spacing={2}>
              <PoetCluster onClick={() => dispatch(setIsOpen(true))} />
            </Grid>
          );
        })}
      </Grid>
    </Stack>
  );
};
