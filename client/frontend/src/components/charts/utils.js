import { deepGet } from '../../lib/utils';

const formatValue = extraValue => {
  if (typeof extraValue === 'number') {
    if (extraValue === Math.floor(extraValue))
      return extraValue;
    return extraValue.toFixed(2);
  }
  return extraValue;
};

export const gradeDistChartTooltipFormatter = (params) => {
  const value = deepGet(params, '0.data.value');
  const key = deepGet(params, '0.data.key');
  const extraData = deepGet(params, '0.data.extra', []);
  const extraDataString = extraData.map(({ label, value }) => `<span style="color: white;">${ label }: ${ formatValue(value) }</span>`).join('<br/>');

  return (
    `<span style="color: white; font-weight: bold;">Nota ${ key }: ${ formatValue(value) } elevi</span> <br/> ${ extraDataString }`
  );
};

export const horizontalBarChartTooltipFormatter = (params, unit="") => {
  const value = deepGet(params, '0.data.value');
  const key = deepGet(params, '0.data.key');
  const extraData = deepGet(params, '0.data.extra', []);
  const extraDataString = extraData.map(({ label, value }) => `<span style="color: white;">${ label }: ${ formatValue(value) }</span>`).join('<br/>');

  return (
    `<span style="color: white; font-weight: bold;">${ key }: ${ formatValue(value) }${unit}</span> <br/> ${ extraDataString }`
  );
};

export const horizontalBarChartGroupedTooltipFormatter = (params, unit="") => {
  const key = deepGet(params, '0.data.key');

  let result = `<span style=" color: white; font-weight: bold;">${key}:</span><br>`;

  params.forEach((param) => {
    const value = deepGet(param, 'data.value');
    const seriesName = deepGet(param, 'seriesName');
    const extraData = deepGet(param, 'data.extra', []);
    const extraDataString = extraData.map(({ label, value }) => `<span style="color: white;  padding-left: 10px"">${ label }: ${ formatValue(value) }</span>`).join('<br/>');

    result += `<span style="color: white; font-weight: bold; padding-left: 10px">${ seriesName }: ${ formatValue(value) }${unit}</span> <br/> ${extraDataString}<br/>`;
  });

  return result;
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