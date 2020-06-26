const initialState = {};


export default function genericStatistics(state = initialState, action) {
  switch (action.type) {
    case 'CHART_LOADING':
      return {
        ...state,
        [action.data.chartName]: { data: null, loading: true },
      };

    case 'CHART_LOADED':
      const { chartName, chartData } = action.data;
      return {
        ...state,
        [chartName]: { data: chartData, loading: false },
      };

    case 'CHART_ERROR':
      return {
        ...state,
        [action.data.chartName]: { data: null, loading: false },
      };

    case 'CHART_RESET':
      return {};

    default:
      return state;
  }
}
