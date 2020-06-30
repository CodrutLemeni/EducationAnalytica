import Typography from "@material-ui/core/Typography";
import React from "react";
import { connect } from "react-redux";

const NotFound = () => {
  return <Typography>Not found</Typography>;
};

export default connect()(NotFound);
