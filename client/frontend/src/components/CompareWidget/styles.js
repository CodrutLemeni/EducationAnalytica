import makeStyles from '@material-ui/core/styles/makeStyles';

export const useStyles = makeStyles(theme => ({
  paper: {
    padding: theme.spacing(2),
  },
  formControl: {
    width: '100%',
  },
  box: {
    marginBottom: theme.spacing(4),
  },
}));
export const useChartSelectStyles = makeStyles(theme => ({
  formControl: {
    width: '100%',
  },
  box: {
    marginBottom: theme.spacing(2),
  },
}));

