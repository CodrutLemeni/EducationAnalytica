import API, { keysToCamel } from '../../api';

export const loadGenericStatistics = (props) => {
  return (dispatch, getState) => {
    Object.entries(props).forEach(([key, value ]) => {
      dispatch({ type: 'CHART_LOADING', data: { chartName: key } });
      API.get(value)
        .then(({ status, data }) => {
          if (status === 200) {
            const actionData = { chartName: key, chartData: keysToCamel(data) };
            dispatch({ type: 'CHART_LOADED', data: actionData });
          } else if (status >= 400 && status < 500) {
            dispatch({ type: 'CHART_ERROR', data: { chartName: key } });
          }
        });
    });
  };
};
