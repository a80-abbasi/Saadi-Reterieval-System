import { Typography, Button, Box, Stack } from "@mui/material";
import { useAppDispatch, useAppSelector } from "../../app/hooks";
import { selectMenu, setEngineStatus } from "../../app/menuReducer";
const buttonList = [
  { text: " option1", type: "opt1" },
  { text: " option2", type: "opt2" },
  { text: " option3", type: "opt3" },
  { text: " option4", type: "opt4" },
  { text: " option5", type: "opt5" },
];
export const NormalOptions = () => {
  const { enginStatus } = useAppSelector(selectMenu);
  const dispatch = useAppDispatch();

  const MyButton = ({
    text,
    type,
    enginStatus,
    onClick,
  }: {
    text: string;
    type: string;
    enginStatus: string;
    onClick: Function;
  }) => {
    return (
      <Button
        variant="contained"
        sx={{
          bgcolor: type === enginStatus ? "#bb002f" : "#280680",
          color: "white",
          px: 3,
          py: 1,
          borderRadius: 4,
          "&:hover": { bgcolor: type === enginStatus ? "#f50057" : "#5e35b1" },
        }}
        onClick={() => onClick(type)}
      >
        <Typography sx={{ fontFamily: "Lalezar-Regular" }}>{text}</Typography>
      </Button>
    );
  };
  const changeEnginStatus = (type: string) => {
    dispatch(setEngineStatus(type));
  };
  return (
    <Box
      display="flex"
      justifyContent="center"
      alignItems="center"
      sx={{ p: 1, borderRadius: 2 }}
      dir="ltr"
      //   minHeight="100vh"
    >
      <Stack
        sx={{ bgcolor: "white", p: 1, borderRadius: 2 }}
        direction="row"
        spacing={2}
        justifyContent="center"
      >
        {buttonList.map((item) => {
          return (
            <MyButton
              text={item.text}
              type={item.type}
              enginStatus={enginStatus}
              onClick={changeEnginStatus}
            />
          );
        })}
      </Stack>
    </Box>
  );
};
