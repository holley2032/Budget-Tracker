import React, { useState } from "react";
import {
  Box,
  Dialog,
  Button,
  FormControl,
  InputLabel,
  Input,
} from "@material-ui/core";
import { useForm, Controller } from "react-hook-form";

const Budget = (profile) => {
  const { control, handleSubmit } = useForm();
  const onSubmit = (data) => console.log(data);
  //(action = "http://localhost:5000/budget");
  //method = "post";

  return (
    <Box>
      <form onSubmit={handleSubmit(onSubmit)}>
        <Controller
          name="name"
          control={control}
          defaultValue=""
          render={({ field }) => (
            <FormControl>
              <InputLabel htmlFor="name">Budget Name</InputLabel>
              <Input {...field} />
            </FormControl>
          )}
        />

        <Button size="large" variant="contained" color="primary" type="submit">
          Submit
        </Button>
      </form>
    </Box>
  );
};

export default Budget;
