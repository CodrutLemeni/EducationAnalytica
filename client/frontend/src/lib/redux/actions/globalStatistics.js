import API, { keysToCamel } from '../../api';
import horizontal_bar_chart_example from '../../../json_examples/horizontal_bar_chart_example'
import mapchart_example from '../../../json_examples/mapchart 2019'

export const loadGlobalGradeDistribution = () => {
  return (dispatch, getState) => {
    dispatch({ type: 'GLOBAL_GRADE_DISTRIBUTION_LOADING' });
    API.get(`/api/grade-distributions/2015`)
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
    // API.get(`/api/statistics/something`)
    //   .then(({ status, data }) => {
    //     if (status === 200) {
    //       dispatch({ type: 'GLOBAL_AVERAGE_GRADE_PER_PROFILE_DISTRIBUTION_LOADED', data: keysToCamel(data) });
    //     } else if (status >= 400 && status < 500) {
    //       dispatch({ type: 'GLOBAL_AVERAGE_GRADE_PER_PROFILE_DISTRIBUTION_ERROR', data: keysToCamel(data) });
    //     }
    //   });
    dispatch({ type: 'GLOBAL_AVERAGE_GRADE_PER_PROFILE_DISTRIBUTION_LOADED', data: horizontal_bar_chart_example });
  };
};

export const loadGlobalAverageGradePerCountyDistribution = () => {
  return (dispatch, getState) => {
    dispatch({ type: 'GLOBAL_AVERAGE_GRADE_PER_COUNTY_DISTRIBUTION_LOADING' });
    // API.get(`/api/statistics/something`)
    //   .then(({ status, data }) => {
    //     if (status === 200) {
    //       dispatch({ type: 'GLOBAL_AVERAGE_GRADE_PER_COUNTY_DISTRIBUTION_LOADED', data: keysToCamel(data) });
    //     } else if (status >= 400 && status < 500) {
    //       dispatch({ type: 'GLOBAL_AVERAGE_GRADE_PER_COUNTY_DISTRIBUTION_ERROR', data: keysToCamel(data) });
    //     }
    //   });
    dispatch({ type: 'GLOBAL_AVERAGE_GRADE_PER_COUNTY_DISTRIBUTION_LOADED', data: mapchart_example });
  };
};

export const loadGlobalHistograms = () => {
  return (dispatch, getState) => {
    dispatch(loadGlobalGradeDistribution());
    dispatch(loadGlobalAverageGradePerProfileDistribution());
    dispatch(loadGlobalAverageGradePerCountyDistribution());
  };
};
