import Box from "@material-ui/core/Box";
import Paper from "@material-ui/core/Paper";
import Typography from "@material-ui/core/Typography";
import React, { useEffect } from "react";
import { connect } from "react-redux";
import { useParams } from "react-router-dom";
import { COUNTIES, isValidCountyCode } from "../../config/countyInfo";
import { useStyles } from "./styles";

const CountyPage = ({ loadCharts }) => {
  const { countyCode } = useParams();
  useEffect(() => {
    if (isValidCountyCode(countyCode)) loadCharts(countyCode);
  }, [loadCharts, countyCode]);
  const classes = useStyles();

  if (!isValidCountyCode(countyCode))
    return (
      <Typography variant="h4" align="center">
        Cod de județ invalid!
      </Typography>
    );

  return (
    <Box>
      <Paper className={classes.titlePaper}>
        <Typography
          variant="h4"
          component={"span"}
          className={classes.whiteText}
        >
          Județul&nbsp;
        </Typography>
        <Typography component={"span"} variant={"h4"} color={"secondary"}>
          {COUNTIES[countyCode]}
        </Typography>
      </Paper>
    </Box>
  );
};

const mapStateToProps = (state) => {
  return {};
};

const mapDispatchToProps = (dispatch) => {
  return {
    loadCharts: (countyCode) => {},
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(CountyPage);
