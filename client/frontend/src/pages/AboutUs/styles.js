import makeStyles from "@material-ui/core/styles/makeStyles";

export const useStyles = makeStyles((theme) => ({
  topBox: {
    backgroundColor: theme.palette.primary.dark,
    paddingTop: 5,
    paddingBottom: 150,
    color: "white",
    width: "99vw",
    position: "relative",
    left: "50%",
    right: "50%",
    marginLeft: "-49.5vw",
    marginRight: "-49.5vw",
    clipPath:
      "polygon(50% 0%, 100% 0px, 100% 70%, 80% 90%, 50.10% 94.07%, 20% 90%, 0% 70%, 0px 0px)",
  },
  title: {
    marginTop: 48,
    textAlign: "center",
  },
  titleName: {
    color: theme.palette.primary.light,
    fontSize: 40,
  },
  subtitle: {
    textAlign: "center",
    fontSize: 20,
  },
  imageGrid: {
    marginTop: 48,
  },
  text: {
    marginTop: 15,
    fontSize: 20,
    textAlign: "left",
    display: "block",
    marginLeft: "auto",
    marginRight: "auto",
    width: "75%",
    lineHeight: "2rem",
    textJustify: "auto",
  },
  logo: {
    display: "block",
    marginLeft: "auto",
    marginRight: "auto",
    width: "70%",
    marginTop: "2rem",
    marginBottom: "2rem",
    maxHeight: "150px",
    maxWidth: "360px",
  },
  contrastText: {
    color: theme.palette.primary.light,
    fontWeight: "bold",
    textAlign: "center",
  },
  [theme.breakpoints.down("xs")]: {
    topBox: {
      clipPath:
        "polygon(50% 0%, 100% 0px, 100% 70%, 90.03% 81.95%, 50.92% 85.19%, 8.35% 81.95%, 0% 70%, 0px 0px)",
      marginBottom: "-100px",
    },
  },
}));
