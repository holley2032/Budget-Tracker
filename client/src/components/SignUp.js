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

//Mask password while being typed in.

const SignUp = ({ openSignUp, handleOpenSignUp }) => {
  const handleSubmitSignUp = () => {
    handleOpenSignUp();
    //Add submitting logic to backend.
  };
  return (
    <div className="SignUp">
      <Button onClick={handleOpenSignUp}>
        <CloseIcon />
      </Button>
      <Box className="Form">
        <FormControl>
          <InputLabel htmlFor="first name">First Name</InputLabel>
          <Input id="first name"></Input>
        </FormControl>
        <FormControl>
          <InputLabel htmlFor="last name">Last Name</InputLabel>
          <Input id="last name"></Input>
        </FormControl>
        <FormControl>
          <InputLabel htmlFor="email address">Email Address</InputLabel>
          <Input id="email address"></Input>
        </FormControl>
        <FormControl>
          <InputLabel htmlFor="password">Password</InputLabel>
          <Input id="password"></Input>
        </FormControl>
        <Button
          onClick={handleSubmitSignUp}
          size="large"
          variant="contained"
          color="primary"
        >
          Submit
        </Button>
      </Box>
    </div>
  );
};

export default SignUp;
