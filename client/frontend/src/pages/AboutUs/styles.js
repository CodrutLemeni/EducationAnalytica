import makeStyles from "@material-ui/core/styles/makeStyles";

export const useStyles = makeStyles((theme) => ({
  topBox: {
    backgroundColor: theme.palette.primary.dark,
    marginLeft: -24,
    marginRight: -24,
    marginTop: -5,
    paddingTop: 10,
    paddingBottom: 150,
    color: "white",
    clipPath: "ellipse(80% 52% at 50% 25%)",
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
    fontSize: 18,
    textAlign: "left",
    display: "block",
    marginLeft: "auto",
    marginRight: "auto",
    width: "75%",
  },
  logo: {
    display: "block",
    marginLeft: "auto",
    marginRight: "auto",
    width: "50%",
  },
  goalsBox: {
    color: "black",
    marginTop: -150,
  },
}));
