import makeStyles from '@material-ui/core/styles/makeStyles';

export const useStyles = makeStyles(theme => ({
  root: {
    margin: theme.spacing(2),
  },
  title: {
    marginBottom: theme.spacing(1),
  },
  content: {
    textIndent: theme.spacing(2),
    textAlign: 'justify',
    textJustify: 'inter-word',
  },
}));

