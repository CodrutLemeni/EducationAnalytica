import { makeStyles } from '@material-ui/core/styles';


export const useStyles = makeStyles(theme => ({
  paper: {
    position: 'relative',
    padding: theme.spacing(1),
    margin: theme.spacing(1),
  },
  title: {
    padding: theme.spacing(1),
    margin: theme.spacing(1),
  },
  subtitle: {
    padding: theme.spacing(1),
  },
}));
