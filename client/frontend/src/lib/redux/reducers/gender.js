const initialState = {
  genderYears: {},
};

export default function gender(state = initialState, action) {
  switch (action.type) {
    case "GENDER_LOADING":
      return {
        ...state,
        genderYears: {
          ...state.genderYears,
          [action.year]: {
            ...state.genderYears[action.year],
            loading: true,
          },
        },
      };

    case "GENDER_LOADED":
      return {
        ...state,
        genderYears: {
          ...state.genderYears,
          [action.year]: {
            ...state.genderYears[action.year],
            loading: false,
            data: action.data,
          },
        },
      };

    case "GENDER_ERROR":
      return {
        ...state,
        genderYears: {
          ...state.genderYears,
          [action.year]: {
            ...state.genderYears[action.year],
            loading: false,
            error: action.data,
          },
        },
      };

    default:
      return state;
  }
}
