import React, { useState } from "react";
import {
  Box,
  Dialog,
  Button,
  FormControl,
  InputLabel,
  Input,
} from "@material-ui/core";

const Budget = (profile) => {
  return (
    <Box>
      <form action="http://localhost:5000/budget" method="post">
        <FormControl>
          <InputLabel htmlFor="budget name">Budget Name</InputLabel>
          <Input id="budget name"></Input>
        </FormControl>
        <Button size="large" variant="contained" color="primary" type="submit">
          Submit
        </Button>
      </form>
    </Box>
  );
};

export default Budget;
