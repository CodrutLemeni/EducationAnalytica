import Typography from "@material-ui/core/Typography";
import React from "react";
import { connect } from "react-redux";

const NotFound = () => {
  return (
    <Typography variant="h1" align="center">
      Not found
    </Typography>
  );
};

export default connect()(NotFound);
