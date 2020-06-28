import API, { keysToCamel } from "../../api";

const years = ["2015", "2016", "2017", "2019"];

export const loadSubjectChoiceForSubjectForYear = (subject, year) => {
  return (dispatch, getState) => {
    dispatch({
      type: `SUBJECT_CHOICE_LOADING`,
      year,
    });

    API.get(
      `/api/horizontal-bar-charts/alegere-subiect-${subject}/${year}`
    ).then(({ status, data }) => {
      if (status === 200) {
        dispatch({
          type: `SUBJECT_CHOICE_LOADED`,
          data: keysToCamel(data),
          year,
        });
      } else if (status >= 400 && status < 500) {
        dispatch({
          type: `SUBJECT_CHOICE_ERROR`,
          data: keysToCamel(data),
          year,
        });
      }
    });
  };
};

export const loadSubjectChoiceForSubject = (subject) => {
  return (dispatch, getState) => {
    years.forEach((year) => {
      dispatch(loadSubjectChoiceForSubjectForYear(subject, year));
    });
  };
};
