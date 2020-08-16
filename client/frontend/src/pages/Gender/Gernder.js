import React from "react";
import { connect } from "react-redux";
import { useEffect } from "react";

import { loadGenderForSubject } from "../../lib/redux/actions/gender";

import { NotFound } from "../";

import { Chart } from "../../components/charts/Chart";
import { TitleBox } from "../../components/TitleBox";
import { Box, Grid } from "@material-ui/core";

const subjects = [
  {
    id: 0,
    label: "Fete vs Baieti",
    code: "fete-baieti",
    options: "",
  },
  {
    id: 1,
    label: "Fete vs baieti mate-info, filologie, stiinte ale naturii",
    code: "fete-baieti-mate-info-filo-si-stiinte",
    options: "",
  },
  {
    id: 2,
    label: "Procentaj promovabilitate fete vs baieti urban si rural",
    code: "procentaj-promovabilitate-fete-baieti-urban-rural",
    options: "",
  },
  {
    id: 3,
    label: "Procentaj alegere profil in functie de sex",
    code: "procentaj-alegere-profil-in-functie-de-sex",
  },
];

function Gernder({ match, genderYears, loadCharts }) {
  const { label, options, code } = subjects.find(
    (sub) => sub.code === match.params.subject
  );
  useEffect(() => loadCharts(code), [loadCharts]);

  if (label === undefined) return <NotFound />;

  return (
    <Box>
      <TitleBox title={label}>Fete vs Baieti</TitleBox>
      <Grid container spacing={5}>
        {Object.entries(genderYears).map(([key, value], index) => (
          <Grid
            item
            xs={12}
            md={code === "procentaj-alegere-profil-in-functie-de-sex" ? 12 : 6}
            key={index}
          >
            <Chart height={500} chartData={value} />
          </Grid>
        ))}
      </Grid>
    </Box>
  );
}

const mapSateToProps = (state) => ({
  genderYears: state.gender.genderYears,
});

const mapDispatchToProps = (dispatch) => ({
  loadCharts: (subject) => {
    dispatch(loadGenderForSubject(subject));
  },
});

export default connect(mapSateToProps, mapDispatchToProps)(Gernder);
