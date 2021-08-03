import React, { useState } from "react";
import { Box, Dialog, Button } from "@material-ui/core";

import Login from "../components/Login";
import SignUp from "../components/SignUp";

const LandingPage = () => {
  const [openLogin, setOpenLogin] = useState(false);
  const [openSignUp, setOpenSignUp] = useState(false);

  const handleOpenLogin = () => {
    setOpenLogin(!openLogin);
  };

  const handleOpenSignUp = () => {
    setOpenSignUp(!openSignUp);
  };

  return (
    <Box>
      <Button
        onClick={handleOpenLogin}
        size="large"
        variant="contained"
        color="secondary"
      >
        Login
      </Button>
      <Button
        onClick={handleOpenSignUp}
        size="large"
        variant="contained"
        color="primary"
      >
        Sign Up
      </Button>
      <Dialog open={openLogin}>
        <Login />
      </Dialog>
      <Dialog open={openSignUp}>
        <SignUp openSignUp={openSignUp} handleOpenSignUp={handleOpenSignUp} />
      </Dialog>
    </Box>
  );
};

export default LandingPage;
