import Fade from "@material-ui/core/Fade";
import React from 'react';
import { CircularProgress } from '@material-ui/core';
import Box from '@material-ui/core/Box';
import useStyles from './styles';

const OverlayCircularProgress = ({ circularSize, color, show }) => {
  const classes = useStyles();

  if (!show)
    return null;

  return <Fade in timeout={ 150 }>
    <Box className={ classes.root }>
      <CircularProgress size={ circularSize } color={ color }/>
    </Box>
  </Fade>;
};
export default OverlayCircularProgress;
