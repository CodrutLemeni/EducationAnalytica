import ReactEcharts from 'echarts-for-react';
import React, { useMemo } from 'react';
import { deepGet } from '../../../lib/utils';
import ChartWrapper from '../ChartWrapper/ChartWrapper';
import { horizontalBarChartGroupedTooltipFormatter } from '../utils';


const BAR_COLORS = [
  { background: '#086972', contrast: '#fff' },
  { background: '#87dfd6', contrast: '#111' },
  { background: '#01a9b4', contrast: '#111' },
];
const DEFAULT_COLOR = BAR_COLORS[0];

const createSeriesConfig = (name, data, colorIndex, unit = '') => {
  const { background, contrast } = deepGet(BAR_COLORS, colorIndex, DEFAULT_COLOR);
  return {
    data,
    name,
    type: 'bar',
    color: background,
    label: {
      show: true,
      formatter: ({ seriesName, name, value }) => `${ seriesName }: ${ value.toFixed(2) }${ unit }`,
      fontSize: 15,
      color: contrast,
    },
  };
};

const HorizontalBarChartGrouped = ({ chartData, height }) => {
  const { seriesList, title, loading, xAxisName, yAxisName, descriptionText } = useMemo(() => ({
    seriesList: deepGet(chartData, 'data.seriesList', []),
    title: deepGet(chartData, 'data.meta.title', []),
    loading: deepGet(chartData, 'loading', true),
    xAxisName: deepGet(chartData, 'data.meta.xAxisName', ''),
    yAxisName: deepGet(chartData, 'data.meta.yAxisName', ''),
    descriptionText: deepGet(chartData, 'data.meta.descriptionText'),
  }), [ chartData ]);


  const yAxisData = useMemo(() => deepGet(seriesList, '0.series', []).map(({ key }) => key), [ seriesList ]);
  const unit = useMemo(() => xAxisName.toLowerCase() === 'procentaj' ? '%' : '', [ xAxisName ]);
  const series = useMemo(() => seriesList.map(({ name, series }, index) => createSeriesConfig(name, series, index, unit)), [ seriesList, unit ]);
  const option = useMemo(() => ({
    grid: {
      left: 70,
    },
    xAxis: [ {
      type: 'value',
      name: xAxisName,
    } ],
    yAxis: [ {
      type: 'category',
      data: yAxisData,
      name: yAxisName,
      inverse: true,
    } ],
    formatter: params => horizontalBarChartGroupedTooltipFormatter(params, unit),
    tooltip: [ {
      trigger: 'axis',
      axisPointer: {
        type: 'line',
      },
    } ],
    series,
  }), [ series, yAxisData, xAxisName, yAxisName, unit ]);


  return <ChartWrapper title={ title } loading={ loading } descriptionText={ descriptionText }>
    <ReactEcharts
      option={ option }
      style={ { height, width: '100%' } }
      opts={ { renderer: 'svg' } }
    />
  </ChartWrapper>;
};


export default HorizontalBarChartGrouped;
