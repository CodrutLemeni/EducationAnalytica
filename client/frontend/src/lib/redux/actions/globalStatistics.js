import API, { keysToCamel } from '../../api';

export const loadGlobalGradeDistribution = () => {
  return (dispatch, getState) => {
    dispatch({ type: 'GLOBAL_GRADE_DISTRIBUTION_LOADING' });
    API.get(`/api/grade-distributions/2019`)
      .then(({ status, data }) => {
        if (status === 200) {
          dispatch({ type: 'GLOBAL_GRADE_DISTRIBUTION_LOADED', data: keysToCamel(data) });
        } else if (status >= 400 && status < 500) {
          dispatch({ type: 'GLOBAL_GRADE_DISTRIBUTION_ERROR', data: keysToCamel(data) });
        }
      });

  };
};

export const loadGlobalAverageGradePerProfileDistribution = () => {
  return (dispatch, getState) => {
    dispatch({ type: 'GLOBAL_AVERAGE_GRADE_PER_PROFILE_DISTRIBUTION_LOADING' });
    API.get(`/api/horizontal-bar-charts/fete-baieti-mate-info-filo-si-stiinte/2019`)
      .then(({ status, data }) => {
        if (status === 200) {
          dispatch({ type: 'GLOBAL_AVERAGE_GRADE_PER_PROFILE_DISTRIBUTION_LOADED', data: keysToCamel(data) });
        } else if (status >= 400 && status < 500) {
          dispatch({ type: 'GLOBAL_AVERAGE_GRADE_PER_PROFILE_DISTRIBUTION_ERROR', data: keysToCamel(data) });
        }
      });

  };
};

export const loadGlobalAverageGradePerCountyDistribution = () => {
  return (dispatch, getState) => {
    dispatch({ type: 'GLOBAL_AVERAGE_GRADE_PER_COUNTY_DISTRIBUTION_LOADING' });
    API.get(`/api/map-charts/2019`)
      .then(({ status, data }) => {
        if (status === 200) {
          dispatch({ type: 'GLOBAL_AVERAGE_GRADE_PER_COUNTY_DISTRIBUTION_LOADED', data: keysToCamel(data) });
        } else if (status >= 400 && status < 500) {
          dispatch({ type: 'GLOBAL_AVERAGE_GRADE_PER_COUNTY_DISTRIBUTION_ERROR', data: keysToCamel(data) });
        }
      });

  };
};

export const loadGlobalHistograms = () => {
  return (dispatch, getState) => {
    dispatch(loadGlobalGradeDistribution());
    dispatch(loadGlobalAverageGradePerProfileDistribution());
    dispatch(loadGlobalAverageGradePerCountyDistribution());
  };
};
