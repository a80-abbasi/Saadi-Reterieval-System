import { Typography, Button, Box, Stack } from "@mui/material";
import { useAppDispatch, useAppSelector } from "../../app/hooks";
import { selectMenu, setEngineStatus } from "../../app/menuReducer";
import { setResult } from "../../app/resultReducer";
import { linkanalysisText } from "../../logic/controller";
const buttonList = ["hits", "page rank"];
export const LinkAnalysis = () => {
  const { enginStatus }: any = useAppSelector(selectMenu);
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
          px: 2,
          py: 1,
          borderRadius: 4,
          "&:hover": { bgcolor: type === enginStatus ? "#f50057" : "#5e35b1" },
        }}
        onClick={() => onClick(type)}
      >
        <Typography sx={{ fontFamily: "Lalezar-Regular", fontSize: 15 }}>
          {text}
        </Typography>
      </Button>
    );
  };
  const changeLink = async (type: string) => {
    try {
      const data = await linkanalysisText(type);
      if (type === "hits") {
        dispatch(setResult(data["authority"]));
      } else {
        dispatch(setResult(data["nodes"]));
      }
      dispatch(setEngineStatus(type));
    } catch (e) {
      console.log("error: ", e);
    }
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
              text={item}
              type={item}
              enginStatus={enginStatus}
              onClick={changeLink}
            />
          );
        })}
      </Stack>
    </Box>
  );
};
