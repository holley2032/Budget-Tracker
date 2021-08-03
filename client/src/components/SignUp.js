import React from "react";
import {
  Box,
  Dialog,
  Button,
  FormControl,
  InputLabel,
  Input,
} from "@material-ui/core";
import CloseIcon from "@material-ui/icons/Close";

const SignUp = ({ openSignUp, handleOpenSignUp }) => {
  return (
    <div className="SignUp">
      <Button onClick={handleOpenSignUp}>
        <CloseIcon />
      </Button>
      <Box className="Form">
        <FormControl>
          <InputLabel htmlFor="email address">Email Address</InputLabel>
          <Input id="email address"></Input>
        </FormControl>
      </Box>
    </div>
  );
};

export default SignUp;
