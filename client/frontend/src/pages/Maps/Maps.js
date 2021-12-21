import React, { useEffect } from "react";
import { connect } from "react-redux";
import { loadMaps } from "../../lib/redux/actions/maps";

import { Chart } from "../../components/charts/Chart";
import { TitleBox } from "../../components/TitleBox";
import {
  Box,
  Card,
  CardContent,
  Typography,
  Grid,
  CardActionArea,
} from "@material-ui/core";

const mapsList = [
  {
    id: 0,
    label: "2015",
    code: "2015",
    options: "Mediile pe judete in anul 2015",
  },
  {
    id: 1,
    label: "2016",
    code: "2016",
    options: "Mediile pe judete in anul 2016",
  },
  {
    id: 2,
    label: "2017",
    code: "2017",
    options: "Mediile pe judete in anul 2017",
  },
  {
    id: 3,
    label: "2019",
    code: "2019",
    options: "Mediile pe judete in anul 2019",
  },
];

function Maps({ maps, loadCharts }) {
  useEffect(() => loadCharts(), [loadCharts]);

  return (
    <Box>
      <TitleBox title={"Media pe judete"}>
        Etiam erat magna, consequat id malesuada sit amet, volutpat id velit.
        Integer non lacus ex. Vivamus ac fringilla nisl. Maecenas aliquet, diam
        et vestibulum molestie, ipsum ipsum scelerisque nunc, at sagittis mi
        enim quis est. Donec auctor leo nec urna blandit, eget placerat arcu
        dictum. Nam ante orci, bibendum eget blandit non, sollicitudin sit amet
        nibh. Phasellus varius tincidunt massa, sed finibus elit sagittis nec.
      </TitleBox>
      <Grid container spacing={5}>
        {Object.entries(maps).map(([key, value], index) => (
          <Grid item xs={12} md={6} key={index}>
            <Chart height={500} chartData={value} />
          </Grid>
        ))}
      </Grid>
    </Box>
  );
}

const mapStateToProps = (state) => ({
  maps: state.maps.maps,
});

const mapDispatchToProps = (dispatch) => ({
  loadCharts: () => {
    dispatch(loadMaps());
  },
});

export default connect(mapStateToProps, mapDispatchToProps)(Maps);
