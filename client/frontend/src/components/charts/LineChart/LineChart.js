import ReactEcharts from 'echarts-for-react';
import React, { useMemo } from 'react';
import { deepGet } from '../../../lib/utils';
import ChartWrapper from '../ChartWrapper/ChartWrapper';


const BAR_COLORS = [
  { background: '#086972', contrast: '#fff' },
  { background: '#87dfd6', contrast: '#111' },
  { background: '#01a9b4', contrast: '#111' },
];
const DEFAULT_COLOR = BAR_COLORS[0];

const createSeriesConfig = (name, data, colorIndex, unit = '') => {
  const { background } = deepGet(BAR_COLORS, colorIndex, DEFAULT_COLOR);
  return {
    data,
    name,
    type: 'line',
    color: background,
    symbolSize: 15,
    lineStyle: {
      color: background,
      width: 5,
    },
  };
};

const titleExtractor = chartDataList => {
  const titles = (chartDataList || []).map((chartData) => deepGet(chartData, 'data.meta.title')).filter(x => !!x);
  if (titles.length === 0) return '';
  if (titles.length <= 2) return titles.join(' VS ');
  return titles.slice(0, 2).join(' VS ') + 'VS ...';
};

const loadingExtractor = chartDataList => {
  return chartDataList.map(({ loading }) => !!loading).reduce((total, currentValue) => total || currentValue);
};

const seriesListExtractor = chartDataList => {
  let result = [];
  (chartDataList || []).forEach((chartData) => {
    const series = deepGet(chartData, 'data.seriesList.0', undefined);
    if (series)
      result.push(series);
  });
  return [ ...result ];
};

const legendExtractor = chartDataList => {
  return (chartDataList || []).map((value) => deepGet(value, 'data.meta.title')).filter(value => !!value);
};

const chartDataExtractor = (chartDataList) => {
  const title = titleExtractor(chartDataList);
  const loading = loadingExtractor(chartDataList);
  const seriesList = seriesListExtractor(chartDataList);
  const legend = legendExtractor(chartDataList);
  return {
    seriesList,
    title,
    loading,
    legend,
    xAxisName: deepGet(chartDataList, '0.data.meta.xAxisName', ''),
    yAxisName: deepGet(chartDataList, '0.data.meta.yAxisName', ''),
  };
};

const LineChart = ({ chartDataList, height, min, max }) => {
  const { seriesList, title, loading, xAxisName, yAxisName, legend } = useMemo(() => chartDataExtractor(chartDataList), [ chartDataList ]);
  const xAxisData = useMemo(() => deepGet(seriesList, '0.series', []).map(({ key }) => key), [ seriesList ]);
  const unit = useMemo(() => xAxisName.toLowerCase() === 'procentaj' ? '%' : '', [ xAxisName ]);
  const series = useMemo(() => seriesList.map(({ name, series }, index) => createSeriesConfig(name, series, index, unit)), [ seriesList, unit ]);

  const option = useMemo(() => ({
    grid: {
      left: 70,
    },
    legend: {
      data: legend,
    },
    xAxis: [ {
      type: 'category',
      name: xAxisName,
      data: xAxisData,
    } ],
    yAxis: [ {
      data: xAxisData,
      type: 'value',
      name: yAxisName,
      min,
      max,
    } ],
    tooltip: [ {
      trigger: 'axis',
    } ],
    series,
  }), [ series, xAxisData, xAxisName, yAxisName, legend ]);

  return <ChartWrapper title={ title } loading={ loading }>
    <ReactEcharts
      option={ option }
      style={ { height, width: '100%' } }
    />
  </ChartWrapper>;
};


export default LineChart;
