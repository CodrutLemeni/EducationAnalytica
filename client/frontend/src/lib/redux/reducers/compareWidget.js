const initialState = {
  series1: null,
  series1Loading: false,
  series1Error: null,

  series2: null,
  series2Loading: false,
  series2Error: null,
};


export default function compareWidget(state = initialState, action) {
  switch (action.type) {
    case 'SERIES_1_LOADING':
      return {
        ...state,
        series1Loading: true,
        series1Error: null,
      };

    case 'SERIES_1_LOADED':
      return {
        ...state,
        series1: action.data,
        series1Loading: false,
        series1Error: null,
      };

    case 'SERIES_1_ERROR':
      return {
        ...state,
        series1: null,
        series1Loading: false,
        series1Error: action.data,
      };


    case 'SERIES_2_LOADING':
      return {
        ...state,
        series2Loading: true,
        series2Error: null,
      };

    case 'SERIES_2_LOADED':
      return {
        ...state,
        series2: action.data,
        series2Loading: false,
        series2Error: null,
      };

    case 'SERIES_2_ERROR':
      return {
        ...state,
        series2: null,
        series2Loading: false,
        series2Error: action.data,
      };

    case 'CLEAR_SERIES':
      return initialState;

    default:
      return state;
  }
}
