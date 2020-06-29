import React, { useEffect } from "react";

import { NotFound } from "../";

import { Chart } from "../../components/charts/Chart";
import { TitleBox } from "../../components/TitleBox";
import { Box, Grid } from "@material-ui/core";

import { connect } from "react-redux";
import { loadSubjectChoiceForSubject } from "../../lib/redux/actions/subjectChoice";
/** Params may be:
 *  filologie, mate-info, resurse-naturale, profil-tehnic, stiinte ale naturii
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
    label: "Profil Tehnic",
    code: "profil-tehnic",
    options: "Fizică, Chimie, Biologie",
  },
  {
    id: 4,
    label: "Profil Resurse naturale şi protecţia mediului",
    code: "profil-resurse-naturale",
    options: "Fizică, Chimie, Biologie",
  },
];

const SubChoice = ({ match, subjectChoiceYears, loadCharts }) => {
  const subject = subjects.find((sub) => sub.code === match.params.subject);
  useEffect(() => loadCharts(subject.code), [loadCharts]);

  if (subject === undefined) return <NotFound />;
  const title = subject.label;

  return (
    <Box>
      <TitleBox title={title}>
        Procentajul de alegere a fiecarei materii pentru subiectul III.
      </TitleBox>
      <Grid container spacing={5}>
        {Object.entries(subjectChoiceYears).map(([key, value], index) => (
          <Grid item xs={12} md={6} key={index}>
            <Chart height={500} chartData={value} />
          </Grid>
        ))}
      </Grid>
    </Box>
  );
};

const mapStateToProps = (state) => {
  return {
    subjectChoiceYears: state.subjectChoice.subjectChoiceYears,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    loadCharts: (subject) => {
      dispatch(loadSubjectChoiceForSubject(subject));
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(SubChoice);
