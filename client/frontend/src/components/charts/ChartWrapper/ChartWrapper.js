import Divider from '@material-ui/core/Divider';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import React from 'react';
import { OverlayCircularProgress } from '../../OverlayCircularProgress';
import { useDescriptionBoxStyles, useStyles } from './styles';


const DescriptionBox = ({ text }) => {
    const classes = useDescriptionBoxStyles();
  return <>
    <Divider variant={ 'middle' }/>
    <Typography variant={ 'h6' } className={classes.typography}>
      { text }
    </Typography>
  </>;
};

const ChartWrapper = ({ title, children, loading, descriptionText }) => {
  const classes = useStyles();
  return <Paper className={ classes.paper }>
    <Typography variant={ 'h4' } className={ classes.title }>
      { title }
    </Typography>
    <Divider variant={ 'middle' }/>
    { children }
    { descriptionText && <DescriptionBox text={ descriptionText } /> }
    <OverlayCircularProgress show={ loading } circularSize={ 100 }/>
  </Paper>;
};

export default ChartWrapper;
