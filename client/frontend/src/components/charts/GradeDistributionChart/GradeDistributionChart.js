import ReactEcharts from 'echarts-for-react';
import React, { useMemo } from 'react';
import { deepGet } from '../../../lib/utils';
import ChartWrapper from '../ChartWrapper/ChartWrapper';
import { gradeDistChartTooltipFormatter } from '../utils';

const round2Decimals = (number) => {
  return Math.floor(Math.round(number * 100)) / 100;
};

//this is temporary, until the backend data is fixed, it will remove the "extra fields"
const EPSILON = 0.00000001;
const groupGradesByInterval = (sortedGradeList, intervalSize) => {
  let currentGroupIndex = 0;
  let result = [ { key: 1, value: 0 } ];
  sortedGradeList.forEach(({ key, value }) => {
    const currentGroupKey = round2Decimals(1 + currentGroupIndex * intervalSize);
    const nextGroupKey = round2Decimals(currentGroupKey + intervalSize);
    if (key >= 1 && key <= 10) {
      if (key >= nextGroupKey - EPSILON) {
        result.push({ key: nextGroupKey, value: 0 });
        currentGroupIndex++;
      }
      result[currentGroupIndex].value += value;
    }
  });
  return result;
};

const GradeDistributionChart = ({ chartData, height }) => {
  const { dataList, title, loading, xAxisName, yAxisName, descriptionText } = useMemo(() => ({
    dataList: deepGet(chartData, 'data.series', []),
    title: deepGet(chartData, 'data.meta.title', []),
    loading: deepGet(chartData, 'loading', true),
    xAxisName: deepGet(chartData, 'data.meta.xAxisName', ''),
    yAxisName: deepGet(chartData, 'data.meta.yAxisName', ''),
    descriptionText: deepGet(chartData, 'data.meta.descriptionText'),
  }), [ chartData ]);

  const sortedDataList = useMemo(() => dataList.sort(({ key: key1 }, { key: key2 }) => key1 - key2), [ dataList ]);
  const groupedDataList = useMemo(() => groupGradesByInterval(sortedDataList, 0.1), [ sortedDataList ]);

  const xAxisData = useMemo(() => groupedDataList.map(({ key }) => key), [ groupedDataList ]);

  const option = useMemo(() => ({
    visualMap: {
      show: false,
      min: 10, //this two values should be in the extra field
      max: 20000,
      inRange: {
        colorLightness: [ 0.3, 0.1 ],
      },
    },
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
    formatter: gradeDistChartTooltipFormatter,
    series: [ {
      data: groupedDataList,
      color: '#01a9b4',
      type: 'bar',
    } ],
  }), [ groupedDataList, xAxisData, xAxisName, yAxisName ]);


  return <ChartWrapper title={ title } loading={ loading } descriptionText={ descriptionText }>
    <ReactEcharts
      option={ option }
      style={ { height, width: '100%' } }
      opts={ { renderer: 'svg' } }
    />
  </ChartWrapper>;
};


export default GradeDistributionChart;
