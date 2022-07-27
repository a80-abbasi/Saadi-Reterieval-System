import { Box, Stack, Typography, Button } from "@mui/material";
import { useAppSelector } from "../../app/hooks";
import { selectResult } from "../../app/resultReducer";
import { SinglePoet } from "./singlePoet";

export const PoetCluster = ({
  onClick,
  data = ["23233", "323dff"],
}: {
  onClick?: any;
  data?: any;
}) => {
  // const { result } = useAppSelector(selectResult);
  // console.log("data: ", data);
  return (
    <Box display="flex" justifyContent="center" alignItems="center" width={700}>
      <Stack
        spacing={1}
        sx={{
          p: 1,
          borderRadius: 2,
          bgcolor: "white",
          width: "100%",
        }}
      >
        {/* <Typography>{JSON.stringify(data)}sdad</Typography> */}
        {data &&
          data.slice(0, 5).map((item:string) => {
            return <SinglePoet item={item} />;
          })}
        {onClick ? (
          <Button
            variant="contained"
            color="success"
            onClick={() => onClick(data)}
          >
            <Typography sx={{ fontFamily: "Lalezar-Regular" }}>
              مرور همه ابیات
            </Typography>{" "}
          </Button>
        ) : null}
      </Stack>
    </Box>
  );
};
