import React, { useEffect } from "react";

import { NotFound } from "../";

import { Chart } from "../../components/charts/Chart";
import { TitleBox } from "../../components/TitleBox";
import { Box, Grid } from "@material-ui/core";

import { connect } from "react-redux";
import { loadGradeDistributionForSubject } from "../../lib/redux/actions/gradeDistribution";
/** Params may be:
 *  filologie, mate-info, stiinte ale naturii, general
 */

const subjects = [
  {
    id: 0,
    label: "Filologie",
    code: "filologie",
    options:
      "Geografie, Logică şi argumentare, Psihologie, Economie, Sociologie, Filosofie",
  },
  {
    id: 1,
    label: "Matematica Informatica",
    code: "mate-info",
    options: "Fizică, Chimie, Biologie, Informatică",
  },
  {
    id: 2,
    label: "Stiinte ale Naturii",
    code: "stiinte-ale-naturii",
    options: "Fizică, Chimie, Biologie, Informatică",
  },
  {
    id: 3,
    label: "General",
    code: "general",
    options: "Toate materiile",
  },
];

const GradeDistrib = ({ match, gradeDistributionYears, loadCharts }) => {
  const { label, options, code } = subjects.find(
    (sub) => sub.code === match.params.subject
  );
  useEffect(() => loadCharts(code), [loadCharts]);

  if (label === undefined) return <NotFound />;

  return (
    <Box>
      <TitleBox title={label}>
        Procentajul de alegere a fiecarei materii pentru subiectul III.
      </TitleBox>
      <Grid container spacing={5}>
        {Object.entries(gradeDistributionYears).map(([key, value], index) => (
          <Grid item xs={12} md={6} key={index}>
            <Chart height={500} chartData={value} />
          </Grid>
        ))}
      </Grid>
    </Box>
  );
};

const mapStateToProps = (state) => ({
  gradeDistributionYears: state.gradeDistribution.gradeDistributionYears,
});

const mapDispatchToProps = (dispatch) => ({
  loadCharts: (subject) => {
    dispatch(loadGradeDistributionForSubject(subject));
  },
});

export default connect(mapStateToProps, mapDispatchToProps)(GradeDistrib);
