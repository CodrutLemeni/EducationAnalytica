import Box from '@material-ui/core/Box';
import Divider from '@material-ui/core/Divider';
import Typography from '@material-ui/core/Typography';
import React from 'react';
import { useStyles } from './styles';

const TitleBox = ({ title, children }) => {
  const classes = useStyles();
  return <Box className={ classes.root }>
    <Typography variant={ 'h2' } className={ classes.title }>{ title }</Typography>
    <Divider/>
    <Typography variant={ 'h5' } component={ 'div' } className={ classes.content }>
      { children }
    </Typography>
  </Box>;
};

export default TitleBox;