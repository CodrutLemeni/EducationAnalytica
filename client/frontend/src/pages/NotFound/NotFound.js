import Typography from '@material-ui/core/Typography';
import React from 'react';
import { withLayout } from '../../components/Layout';

const NotFound = () => {
  return <Typography>
    Not found
  </Typography>;
};

export default withLayout(NotFound);

