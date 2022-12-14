import { Stack, Typography } from "@mui/material";

export const SinglePoet = ({ item }: { item: any }) => {
  return (
    <Stack
      sx={{ bgcolor: "wheat", p: 1.5, borderRadius: 2 }}
      direction="row"
      justifyContent={"center"}
    >
      <Typography sx={{ fontFamily: "Lalezar-Regular", fontSize: 22 }}>
        {item}
      </Typography>
    </Stack>
  );
};
