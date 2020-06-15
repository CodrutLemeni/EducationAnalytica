import makeStyles from '@material-ui/core/styles/makeStyles';

export const useStyles = makeStyles(theme => ({
  titlePaper: {
    margin: theme.spacing(1),
    padding: theme.spacing(3),
    background: theme.palette.primary.main,
  },
  whiteText: {
    color: theme.palette.primary.contrastText,
  },

}));
