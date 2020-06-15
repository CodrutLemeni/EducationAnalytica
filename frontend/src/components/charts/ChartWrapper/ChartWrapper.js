import Divider from '@material-ui/core/Divider';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import React from 'react';
import { OverlayCircularProgress } from '../../OverlayCircularProgress';
import { useStyles } from './styles';


const ChartWrapper = ({ title, children,  loading }) => {
  const classes = useStyles();
  return <Paper className={ classes.paper }>
    <Typography variant={ 'h5' } className={ classes.title }>
      { title }
    </Typography>
    <Divider variant={ 'middle' }/>
    { children }
    <OverlayCircularProgress show={ loading } circularSize={ 100 }/>
  </Paper>;
};

export default ChartWrapper;
