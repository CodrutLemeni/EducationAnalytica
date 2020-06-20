import React, { useMemo } from 'react';
import { deepGet } from '../../../lib/utils';
import { CountryChart } from '../CountryChart';
import { GradeDistributionChart } from '../GradeDistributionChart';
import { HorizontalBarChart } from '../HorizontalBarChart';
import { ChartTypes } from '../types';

const chartTypeToComponent = {
  [ChartTypes.GRADE_DIST]: GradeDistributionChart,
  [ChartTypes.HORIZONTAL_BAR_CHART]: HorizontalBarChart,
  [ChartTypes.MAP_CHART]: CountryChart,
};

const Chart = ({ chartData, height }) => {
  const ChartComponent = useMemo(() => {
    const chartMetaType = deepGet(chartData, 'data.meta.type');
    return deepGet(chartTypeToComponent, chartMetaType);
  }, [ chartData ]);

  if (ChartComponent)
    return <ChartComponent chartData={ chartData } height={ height }/>;

  return <>
    Error determining chart type.
  </>;

};

export default Chart;
