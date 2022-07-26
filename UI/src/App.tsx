import "./App.css";
import { theme } from "./config/theme";
import { MainPage } from "./features/pages/mainpage";
import { ThemeProvider } from "@mui/material/styles";

function App() {
  return (
    <ThemeProvider theme={theme}>
      <div className="App">
        <header className="App-header">
          <MainPage />
        </header>
      </div>
    </ThemeProvider>
  );
}

export default App;
