import { Box, Stack, Typography } from "@mui/material";
import RadioButtonCheckedIcon from "@mui/icons-material/RadioButtonChecked";
const MyRow = ({ text }: { text: string }) => {
  return (
    <Stack direction={"row"} spacing={2}>
      <RadioButtonCheckedIcon />
      <Typography sx={{ textAlign: "right", fontFamily: "B-NAZANIN" }}>
        {text}
      </Typography>
    </Stack>
  );
};
export const Help = () => {
  return (
    <Box sx={{ maxWidth: 600, bgcolor: "#b0bec5", p: 2, borderRadius: 5 }}>
      <Stack spacing={1} alignItems="flex-start">
        <MyRow text="این صفحه یک دمو از برنامه بازیابی اطلاعات برای اشعار و متون کتاب های بوستان و گلستان است." />
        <MyRow text="برای انجام جستجو کافیست تا عبارت مورد نظر خود را در مستطیل بالا وارد کنید و گزینه مورد نظر خود را انتخاب کنید." />
        <MyRow
          text="این پروژه توسط تیم کیومرث به سر انجام رسیده که شامل اعضای زیر می باشد:
          علی عباسی، جواد هزاره، امیرعلی ابراهیم زاده، متین شجاع، مازیار شمسی پور و یاسین موسوی"
        />
        <MyRow text="لطفا در کانال ما عضو شوید: @Qmars" />
      </Stack>
    </Box>
  );
};
