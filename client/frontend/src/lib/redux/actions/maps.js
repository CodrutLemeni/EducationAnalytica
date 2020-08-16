import API, { keysToCamel } from "../../api";

const years = ["2015", "2016", "2017", "2019"];

export const loadMapForYear = (year) => {
  return (dispatch, getState) => {
    dispatch({
      type: "MAP_LOADING",
      year,
    });

    API.get(`/api/map-charts/${year}`).then(({ status, data }) => {
      if (status === 200) {
        dispatch({
          type: "MAP_LOADED",
          data: keysToCamel(data),
          year,
        });
      } else if (status >= 400 && status < 500) {
        dispatch({
          type: "MAP_ERROR",
          data: keysToCamel(data),
          year,
        });
      }
    });
  };
};

export const loadMaps = () => {
  return (dispatch, getState) => {
    years.forEach((year) => {
      dispatch(loadMapForYear(year));
    });
  };
};
