import Box from '@material-ui/core/Box';
import Typography from '@material-ui/core/Typography';
import React from 'react';
import { useStyles } from './styles';

const ArticleBox = ({ title, children }) => {
  const classes = useStyles();
  return <Box className={ classes.root }>
    <Typography variant={ 'h4' } className={ classes.title }>{ title }</Typography>
    <Typography variant={ 'h6' } component={ 'div' } className={ classes.content }>
      { children }
    </Typography>
  </Box>;
};

export default ArticleBox;