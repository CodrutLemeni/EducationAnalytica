import { deepGet } from '../../lib/utils';

const formatValue = extraValue => {
  if (typeof extraValue === 'number') {
    if (extraValue === Math.floor(extraValue))
      return extraValue;
    return extraValue.toFixed(2);
  }


  return extraValue;
};

export const barChartTooltipFormatter = (params) => {
  const value = deepGet(params, '0.data.value');
  const key = deepGet(params, '0.data.key');
  const extraData = deepGet(params, '0.data.extra', []);
  const extraDataString = extraData.map(({ label, value }) => `<span style="color: white;">${ label }: ${ formatValue(value) }</span>`).join('<br/>');

  return (
    `<span style="color: white; font-weight: bold;">${ key }: ${ formatValue(value) }%</span> <br/> ${ extraDataString }`
  );
};
export const mapChartTooltipFormatter = (params) => {
  const value = deepGet(params, 'data.value');
  const key = deepGet(params, 'data.name');
  const extraData = deepGet(params, 'data.extra', []);

  const extraDataString = extraData.map(({ label, value }) => `<span style="color: white; ">${ label }: ${ formatValue(value) }</span>`).join('<br/>');

  return (
    `<span style="color: white; font-weight: bold;">${ key }: ${ formatValue(value) }</span> <br/> ${ extraDataString }`
  );
};