import ReactEcharts from 'echarts-for-react';
import React, { useMemo } from 'react';
import { deepGet } from '../../../lib/utils';
import ChartWrapper from '../ChartWrapper/ChartWrapper';
import { horizontalBarChartTooltipFormatter } from '../utils';


const HorizontalBarChart = ({ chartData, height }) => {
  const { dataList, title, loading, xAxisName, yAxisName, descriptionText } = useMemo(() => ({
    dataList: deepGet(chartData, 'data.series', []),
    title: deepGet(chartData, 'data.meta.title', []),
    loading: deepGet(chartData, 'loading', true),
    xAxisName: deepGet(chartData, 'data.meta.xAxisName', ''),
    yAxisName: deepGet(chartData, 'data.meta.yAxisName', ''),
    descriptionText: deepGet(chartData, 'data.meta.descriptionText'),
  }), [ chartData ]);

  const yAxisData = useMemo(() => dataList.map(({ key }) => key), [ dataList ]);
  const unit = useMemo(() => xAxisName.toLowerCase() === 'procentaj' ? '%' : '', [ xAxisName ]);

  const option = useMemo(() => ({
    grid: {
      left: 130,
    },
    xAxis: [ {
      type: 'value',
      name: xAxisName,
    } ],
    yAxis: [ {
      type: 'category',
      data: yAxisData,
      name: yAxisName,
    } ],
    tooltip: [ {
      trigger: 'axis',
      axisPointer: {
        type: 'line',
      },
    } ],
    formatter: (params) => horizontalBarChartTooltipFormatter(params, unit),
    series: [ {
      data: dataList,
      type: 'bar',
      color: '#01a9b4',
    } ],
  }), [ dataList, yAxisData, xAxisName, yAxisName, unit ]);


  return <ChartWrapper title={ title } loading={ loading } descriptionText={ descriptionText }>
    <ReactEcharts
      option={ option }
      style={ { height, width: '100%' } }
      opts={ { renderer: 'svg' } }
    />
  </ChartWrapper>;
};


export default HorizontalBarChart;
