const initialState = {
  gradeDistribution: null,
  gradeDistributionLoading: false,
  gradeDistributionErrors: null,

  averageGradePerProfileDistribution: null,
  averageGradePerProfileDistributionLoading: false,
  averageGradePerProfileDistributionErrors: null,

  averageGradePerCountyDistribution: null,
  averageGradePerCountyDistributionLoading: false,
  averageGradePerCountyDistributionErrors: null,
};

export default function global_statistics(state = initialState, action) {
  switch (action.type) {
    case "GLOBAL_GRADE_DISTRIBUTION_LOADING":
      return {
        ...state,
        gradeDistributionLoading: true,
        gradeDistributionErrors: null,
      };
    case "GLOBAL_GRADE_DISTRIBUTION_LOADED":
      return {
        ...state,
        gradeDistribution: action.data,
        gradeDistributionLoading: false,
        gradeDistributionErrors: null,
      };
    case "GLOBAL_GRADE_DISTRIBUTION_ERROR":
      return {
        ...state,
        gradeDistributionLoading: false,
        gradeDistributionErrors: action.data,
      };

    case "GLOBAL_AVERAGE_GRADE_PER_PROFILE_DISTRIBUTION_LOADING":
      return {
        ...state,
        averageGradePerProfileDistributionLoading: true,
        averageGradePerProfileDistributionErrors: null,
      };
    case "GLOBAL_AVERAGE_GRADE_PER_PROFILE_DISTRIBUTION_LOADED":
      return {
        ...state,
        averageGradePerProfileDistribution: action.data,
        averageGradePerProfileDistributionLoading: false,
        averageGradePerProfileDistributionErrors: null,
      };
    case "GLOBAL_AVERAGE_GRADE_PER_PROFILE_DISTRIBUTION_ERROR":
      return {
        ...state,
        averageGradePerProfileDistributionLoading: false,
        averageGradePerProfileDistributionErrors: action.data,
      };

    case "GLOBAL_AVERAGE_GRADE_PER_COUNTY_DISTRIBUTION_LOADING":
      return {
        ...state,
        averageGradePerCountyDistributionLoading: true,
        averageGradePerCountyDistributionErrors: null,
      };
    case "GLOBAL_AVERAGE_GRADE_PER_COUNTY_DISTRIBUTION_LOADED":
      return {
        ...state,
        averageGradePerCountyDistribution: action.data,
        averageGradePerCountyDistributionLoading: false,
        averageGradePerCountyDistributionErrors: null,
      };
    case "GLOBAL_AVERAGE_GRADE_PER_COUNTY_DISTRIBUTION_ERROR":
      return {
        ...state,
        averageGradePerCountyDistributionLoading: false,
        averageGradePerCountyDistributionErrors: action.data,
      };

    default:
      return state;
  }
}
