import API, { keysToCamel } from '../../api';

export const loadSeries1 = (url) => {
  return (dispatch, getState) => {
    dispatch({ type: 'SERIES_1_LOADING' });
    API.get(url)
      .then(({ status, data }) => {
        if (status === 200) {
          dispatch({ type: 'SERIES_1_LOADED', data: keysToCamel(data) });
        } else if (status >= 400 && status < 500) {
          dispatch({ type: 'SERIES_1_ERROR', data: keysToCamel(data) });
        }
      });
  };
};

export const loadSeries2 = (url) => {
  return (dispatch, getState) => {
    dispatch({ type: 'SERIES_2_LOADING' });
    API.get(url)
      .then(({ status, data }) => {
        if (status === 200) {
          dispatch({ type: 'SERIES_2_LOADED', data: keysToCamel(data) });
        } else if (status >= 400 && status < 500) {
          dispatch({ type: 'SERIES_2_ERROR', data: keysToCamel(data) });
        }
      });
  };
};

export const clearSeries = () => ({type: 'CLEAR_SERIES'});