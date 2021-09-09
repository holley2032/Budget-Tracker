import React, { Fragment } from "react";
import { MuiThemeProvider } from "@material-ui/core";
import CssBaseline from "@material-ui/core/CssBaseline";
import { BrowserRouter, Route } from "react-router-dom";
import theme from "./themes/theme";
import "./App.css";
import LandingPage from "./pages/LandingPage";
import Budget from "./components/Budget";

const App = () => {
  return (
    <Fragment>
      <CssBaseline>
        <MuiThemeProvider theme={theme}>
          <BrowserRouter>
            <Route path="/" component={Budget} />
          </BrowserRouter>
        </MuiThemeProvider>
      </CssBaseline>
    </Fragment>
  );
};

export default App;
