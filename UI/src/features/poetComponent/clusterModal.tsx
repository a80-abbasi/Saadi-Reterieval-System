import * as React from "react";
import Backdrop from "@mui/material/Backdrop";
import Box from "@mui/material/Box";
import Modal from "@mui/material/Modal";
import { List } from "@mui/material";

import Fade from "@mui/material/Fade";
import Button from "@mui/material/Button";
import {Stack} from "@mui/material";
import Typography from "@mui/material/Typography";
import { SinglePoet } from "./singlePoet";
import { useAppDispatch, useAppSelector } from "../../app/hooks";
import { selectResult, setIsOpen } from "../../app/resultReducer";
import { useDispatch } from "react-redux";

const style = {
  position: "absolute" as "absolute",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  width: "50vw",
  height: "70vh",
  bgcolor: "background.paper",
  border: "0px solid #000",
  boxShadow: 24,
  p: 4,
  overflow: "auto"
};

export function ClusterModal() {
  const resultState = useAppSelector(selectResult);
  const dispatch = useAppDispatch();
  const handleClose = () => {
    dispatch(setIsOpen(false))
  };


  return (
    <div>
      <Modal
        aria-labelledby="transition-modal-title"
        aria-describedby="transition-modal-description"
        open={resultState.isOpen}
        onClose={handleClose}
        closeAfterTransition
        BackdropComponent={Backdrop}
        BackdropProps={{
          timeout: 500,
        }}
      >
        <Fade in={resultState.isOpen}>
          <Box sx={style}>
            <Stack spacing={1} >
              {[...Array(30)].map((e) => (
                <SinglePoet item={{ text: `${e}` }} />
              ))}
            </Stack>
          </Box>
        </Fade>
      </Modal>
    </div>
  );
}
