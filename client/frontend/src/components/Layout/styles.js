import makeStyles from "@material-ui/core/styles/makeStyles";

export const useStyles = makeStyles((theme) => ({
  root: {
    minHeight: "100vh",
    display: "flex",
    flexDirection: "column",
  },
  container: {
    display: "flex",
    flexGrow: 1,
    flexDirection: "column",
  },
}));

export const useLayoutHeaderStyle = makeStyles((theme) => ({
  appBar: {
    padding: theme.spacing(1, 1),
    background: theme.palette.primary.dark,
  },
  inline: {
    display: "inline",
  },
  link: {
    "&$link": {
      textDecoration: "none",
      color: "inherit",
    },
  },
  navLink: {
    "&:hover": {
      color: theme.palette.secondary.light,
    },
  },
  navLinkActive: {
    "&$link": {
      color: theme.palette.secondary.dark,
    },
  },
  flexExpander: {
    flex: 1,
  },
  navText: {
    padding: theme.spacing(0, 1),
  },
  tab: {
    maxWidth: 100,
  },
}));
