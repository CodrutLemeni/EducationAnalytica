import API, { keysToCamel } from "../../api";

const years = ["2015", "2016", "2017", "2019"];

export const loadGenderForSubjectForYear = (subject, year) => {
  return (dispatch, getState) => {
    dispatch({
      type: "GENDER_LOADING",
      year,
    });

    API.get(`/api/horizontal-bar-charts/${subject}/${year}`).then(
      ({ status, data }) => {
        if (status === 200) {
          dispatch({
            type: "GENDER_LOADED",
            data: keysToCamel(data),
            year,
          });
        } else if (status >= 400 && status < 500) {
          dispatch({
            type: `GENDER_ERROR`,
            data: keysToCamel(data),
            year,
          });
        }
      }
    );
  };
};

export const loadGenderForSubject = (subject) => {
  if (subject === undefined) return;
  return (dispatch, getState) => {
    years.forEach((year) => {
      dispatch(loadGenderForSubjectForYear(subject, year));
    });
  };
};
