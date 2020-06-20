import makeStyles from '@material-ui/core/styles/makeStyles';

export const useStyles = makeStyles((theme) => ({
}));

export const useCountyTableStyles = makeStyles((theme) => ({
  paper: {
    margin: theme.spacing(1),
  },
  table: {
    padding: theme.spacing(1),
  },
  tableHead: {
    background: theme.palette.primary.main,
  },
  tableHeaderCell: {
    color: 'white',
    fontSize: 25,
    padding: theme.spacing(2),
  },
  dataCell: {
    fontSize: 15,
  },
}));
