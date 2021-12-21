import Paper from "@material-ui/core/Paper";
import Typography from "@material-ui/core/Typography";
import React, { useMemo } from "react";
import { deepGet } from "../../../lib/utils";
import { CountryChart } from "../CountryChart";
import { GradeDistributionChart } from "../GradeDistributionChart";
import { HorizontalBarChartGrouped } from "../HorinzontalBarChartGrouped";
import { HorizontalBarChartStacked } from "../HorinzontalBarChartStacked";
import { HorizontalBarChart } from "../HorizontalBarChart";
import { ChartTypes } from "../types";
import { useStyles } from "./styles";

const chartTypeToComponent = {
  [ChartTypes.GRADE_DIST]: GradeDistributionChart,
  [ChartTypes.HORIZONTAL_BAR_CHART]: HorizontalBarChart,
  [ChartTypes.MAP_CHART]: CountryChart,
  [ChartTypes.HORIZONTAL_BAR_CHART_GROUPED]: HorizontalBarChartGrouped,
  [ChartTypes.HORIZONTAL_BAR_CHART_STACKED]: HorizontalBarChartStacked,
};

const Chart = ({ chartData, height }) => {
  const classes = useStyles({ height });
  const ChartComponent = useMemo(() => {
    const chartMetaType = deepGet(chartData, "data.meta.type");
    return deepGet(chartTypeToComponent, chartMetaType);
  }, [chartData]);

  if (ChartComponent)
    return <ChartComponent chartData={chartData} height={height} />;

  return (
    <Paper className={classes.errorPaper}>
      <Typography component={"div"} variant={"h4"}>
        Error determining chart type.
      </Typography>
    </Paper>
  );
};

export default Chart;
