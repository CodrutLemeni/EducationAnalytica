import ReactEcharts from 'echarts-for-react';
import React, { useMemo } from 'react';
import { COUNTIES } from '../../../config/countyInfo';
import { deepGet } from '../../../lib/utils';
import ChartWrapper from '../ChartWrapper/ChartWrapper';
import { mapChartTooltipFormatter } from '../utils';


const CountryChart = ({ chartData, height }) => {
  const { dataList, title, loading } = useMemo(() => ({
    dataList: deepGet(chartData, 'data.series', []),
    title: deepGet(chartData, 'data.meta.title', []),
    loading: deepGet(chartData, 'loading', true),
  }), [ chartData ]);

  const formattedList = useMemo(() => dataList.map(({ key, value, ...other }) => ({
    ...other,
    name: COUNTIES[key],
    value,
  })), [ dataList ]);

  const { minValue, maxValue } = useMemo(() => {
    if (dataList.length === 0)
      return { minValue: 0, maxValue: 0 };

    const grades = dataList.map(({ value }) => value);
    console.log(grades);
    const minValue = Math.min(...grades) || 0;
    const maxValue = Math.max(...grades) || 10;

    return { minValue, maxValue };
  }, [ dataList ]);


  const option = useMemo(() => ({
    series: {
      type: 'map',
      mapType: 'RO',
      emphasis: {
        label: {
          show: false,
        },
        itemStyle: {
          areaColor: '#aaaaaa',
          borderWidth: 2,
          borderColor: '#481d1d',
        },
      },
      data: formattedList,
    },
    tooltip: {
      trigger: 'item',
      formatter: mapChartTooltipFormatter,
    },

    visualMap: {
      min: minValue,
      max: maxValue,
      calculable: true,
      realtime: false,
      inRange: {
        color: [ '#ff3333', '#fff900', '#00ea08' ],
      },
    },
  }), [ formattedList, maxValue, minValue ]);

  return <ChartWrapper title={ title } loading={ loading }>
    <ReactEcharts
      option={ option }
      style={ { height, width: '100%' } }
      opts={ { renderer: 'svg' } }
    />
  </ChartWrapper>;
};


export default CountryChart;
