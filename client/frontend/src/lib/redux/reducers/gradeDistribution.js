const initialState = {
  gradeDistributionYears: {},
};

export default function gradeDistribution(state = initialState, action) {
  switch (action.type) {
    case "GRADE_DISTRIBUTION_LOADING":
      return {
        ...state,
        gradeDistributionYears: {
          ...state.gradeDistributionYears,
          [action.year]: {
            ...state.gradeDistributionYears[action.year],
            loading: true,
          },
        },
      };

    case "GRADE_DISTRIBUTION_LOADED":
      return {
        ...state,
        gradeDistributionYears: {
          ...state.gradeDistributionYears,
          [action.year]: {
            ...state.gradeDistributionYears[action.year],
            data: action.data,
            loading: false,
          },
        },
      };

    case "GRADE_DISTRIBUTION_ERROR":
      return {
        ...state,
        gradeDistributionYears: {
          ...state.gradeDistributionYears,
          [action.year]: {
            ...state.gradeDistributionYears[action.year],
            error: action.data,
            loading: false,
          },
        },
      };

    default:
      return state;
  }
}
