import ReactEcharts from 'echarts-for-react';
import moment from 'moment';
import React, { useMemo } from 'react';
import { COUNTIES } from '../../../config/countyInfo';
import { deepGet } from '../../../lib/utils';
import ChartWrapper from '../ChartWrapper/ChartWrapper';


const CountryChart = ({ data, loading, title, height }) => {
  const { dateModified, sampleSize, dataList, average_group, min_group, max_group } = useMemo(() => ({
    dateModified: deepGet(data, 'dateModified'),
    searchString: deepGet(data, 'searchString'),
    sampleSize: deepGet(data, 'content.aggregation.sampleSize'),
    min_group: deepGet(data, 'content.aggregation.minGroupValue', 0),
    max_group: deepGet(data, 'content.aggregation.maxGroupValue', 0),
    average_group: deepGet(data, 'content.aggregation.averageGroupValue', 0),
    dataList: deepGet(data, 'content.data', []),
  }), [ data ]);

  const chartData = useMemo(() => dataList.map(({ label, value }) => ({ name: COUNTIES[label], value })), [ dataList ]);

  const option = useMemo(() => ({
    series: {
      type: 'map',
      mapType: 'RO',
      emphasis: {
        label: {
          show: false,
        },
        itemStyle: {
          areaColor: {
            type: 'radial',
            x: 0.5,
            y: 0.5,
            r: 0.5,
            colorStops: [ { offset: 0, color: '#ff3333' }, { offset: 1, color: '#883333' } ],
          },
          borderWidth: 2,
          borderColor: '#481d1d',
        },
      },
      data: chartData,
    },
    tooltip: {
      trigger: 'item',
      formatter: (item) => `<strong>${ item.name }</strong></br>
          Decese: ${ item.value }</br>`,
    },
    visualMap: {
      min: 0,
      max: max_group,
      calculable: true,
      realtime: false,
      inRange: {
        color: [ '#ddcccc', '#990000', '#330000' ],
      },
    },
  }), [ max_group, chartData ]);


  const metadataList = useMemo(() => [
    { label: 'Numărul minim/județ', value: min_group.toFixed(2) },
    { label: 'Numărul maxim/județ', value: max_group.toFixed(2) },
    { label: 'Numărul mediu/județ', value: average_group.toFixed(2) },
    { label: 'Numărul cazurilor analizate', value: sampleSize },
    { label: 'Ultima actualizare', value: moment(dateModified).format('DD-MM-YYYY') },
  ], [ min_group, max_group, sampleSize, dateModified, average_group ]);

  return <ChartWrapper title={ title } loading={ loading } metadataList={ metadataList }>
    <ReactEcharts
      option={ option }
      style={ { height, width: '100%' } }
      opts={ { renderer: 'svg' } }
    />
  </ChartWrapper>;
};


export default CountryChart;
