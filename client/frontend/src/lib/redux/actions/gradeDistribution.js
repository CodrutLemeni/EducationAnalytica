import API, { keysToCamel } from "../../api";

const years = ["2015", "2016", "2017", "2019"];

export const loadGradeDistributionForSubjectForYear = (subject, year) => {
  return (dispatch, getState) => {
    dispatch({
      type: `GRADE_DISTRIBUTION_LOADING`,
      year,
    });

    API.get(`/api/grade-distributions/${subject}/${year}`).then(
      ({ status, data }) => {
        if (status === 200) {
          dispatch({
            type: `GRADE_DISTRIBUTION_LOADED`,
            data: keysToCamel(data),
            year,
          });
        } else if (status >= 400 && status < 500) {
          dispatch({
            type: `GRADE_DISTRIBUTION_ERROR`,
            data: keysToCamel(data),
            year,
          });
        }
      }
    );
  };
};

export const loadGradeDistributionForSubject = (subject) => {
  if (subject === undefined) return;
  return (dispatch, getState) => {
    years.forEach((year) => {
      dispatch(loadGradeDistributionForSubjectForYear(subject, year));
    });
  };
};
