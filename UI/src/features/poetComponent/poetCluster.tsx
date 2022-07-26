import { Box, Stack, Typography, Button } from "@mui/material";
import { useAppSelector } from "../../app/hooks";
import { selectResult } from "../../app/resultReducer";
import { SinglePoet } from "./singlePoet";

export const PoetCluster = ({ onClick }: { onClick?: any }) => {
  const { result } = useAppSelector(selectResult);

  return (
    <Box display="flex" justifyContent="center" alignItems="center" width={630}>
      <Stack
        spacing={1}
        sx={{
          p: 1,
          borderRadius: 2,
          bgcolor: "white",
          width: "100%",
        }}
      >
        {result.map((item) => {
          return <SinglePoet item={item} />;
        })}
        {onClick ? (
          <Button variant="contained" color="success" onClick={onClick}>
            <Typography sx={{ fontFamily: "Lalezar-Regular" }}>
              {" "}
              مرور همه ابیات
            </Typography>{" "}
          </Button>
        ) : null}
      </Stack>
    </Box>
  );
};
