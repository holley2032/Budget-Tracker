import React from "react";
import { MuiThemeProvider } from "@material-ui/core";
import CssBaseline from "@material-ui/core/CssBaseline";
import { BrowserRouter, Route } from "react-router-dom";

import theme from "themes/theme";
import "./App.css";
import LandingPage from "pages/LandingPage";

const App = () => {
  return (
    <Fragment>
      <CssBaseline>
        <MuiThemeProvider theme={theme}>
          <BrowserRouter>
            <Route path="/" component={LandingPage} />
          </BrowserRouter>
        </MuiThemeProvider>
      </CssBaseline>
    </Fragment>
  );
};

export default App;
