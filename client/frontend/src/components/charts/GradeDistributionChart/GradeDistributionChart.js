import ReactEcharts from 'echarts-for-react';
import React, { useMemo } from 'react';
import { deepGet } from '../../../lib/utils';
import ChartWrapper from '../ChartWrapper/ChartWrapper';
import { barChartTooltipFormatter } from '../utils';


const GradeDistributionChart = ({ chartData, height }) => {
  const { dataList, title, loading, xAxisName, yAxisName } = useMemo(() => ({
    dataList: deepGet(chartData, 'data.series', []),
    title: deepGet(chartData, 'data.meta.title', []),
    loading: deepGet(chartData, 'loading', true),
    xAxisName: deepGet(chartData, 'data.meta.xAxisName', ''),
    yAxisName: deepGet(chartData, 'data.meta.yAxisName', ''),
  }), [ chartData ]);

  const sortedDataList = useMemo(() => dataList.sort(({ key: key1 }, { key: key2 }) => key1 - key2), [ dataList ]);
  const xAxisData = useMemo(() => sortedDataList.map(({ key }) => key), [ sortedDataList ]);
  const option = useMemo(() => ({
    xAxis: [ {
      type: 'category',
      data: xAxisData,
      name: xAxisName,
    } ],
    yAxis: [ {
      type: 'value',
      name: yAxisName,
    } ],
    tooltip: [ {
      trigger: 'axis',
      axisPointer: {
        type: 'line',
      },
    } ],
    formatter: barChartTooltipFormatter,
    series: [ {
      data: sortedDataList,
      type: 'bar',
    } ],
  }), [ sortedDataList, xAxisData, xAxisName, yAxisName ]);


  return <ChartWrapper title={ title } loading={ loading }>
    <ReactEcharts
      option={ option }
      style={ { height, width: '100%' } }
      opts={ { renderer: 'svg' } }
    />
  </ChartWrapper>;
};


export default GradeDistributionChart;
