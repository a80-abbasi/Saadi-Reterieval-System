import * as React from "react";
import TextField from "@mui/material/TextField";
import Autocomplete, { createFilterOptions } from "@mui/material/Autocomplete";
import { expansionText } from "../../logic/controller";

export function AutoComplete({
  value2,
  onChange,
}: {
  value2: string;
  onChange: Function;
}) {
  const [suggestions, setSuggestions] = React.useState<string[]>([]);

  return (
    <React.Fragment>
      <Autocomplete
        value={value2}
        sx={{
          ml: 1,
          flex: 1,
          "& input::placeholder": {
            fontFamily: "Lalezar-Regular",
          },
          border: "0px solid #900",
          outline: "none",
        }}
        onInputChange={async (event, newValue) => {
          console.log("new value: ", newValue);
          onChange(newValue);
          const result = await expansionText(newValue);
          const arr = [result.result];
          console.log("data from search", result);
          setSuggestions(arr);
        }}
        filterOptions={(options, params) => {
          return options;
        }}
        id="free-solo-dialog-demo"
        options={suggestions}
        getOptionLabel={(option) => {
          return option;
        }}
        noOptionsText={"..."}
        renderOption={(props, option) => <li {...props}>{option}</li>}
        renderInput={(params) => <TextField {...params} sx={{fontFamily:"B-NAZANIN"}} />}
      />
    </React.Fragment>
  );
}
