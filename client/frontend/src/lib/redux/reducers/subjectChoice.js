const initialState = {
  subjectChoiceYears: {},
};

export default function subjectChoice(state = initialState, action) {
  switch (action.type) {
    case "SUBJECT_CHOICE_LOADING":
      return {
        ...state,
        subjectChoiceYears: {
          ...state.subjectChoiceYears,
          [action.year]: {
            ...state.subjectChoiceYears[action.year],
            loading: true,
          },
        },
      };

    case "SUBJECT_CHOICE_LOADED":
      return {
        ...state,
        subjectChoiceYears: {
          ...state.subjectChoiceYears,
          [action.year]: {
            ...state.subjectChoiceYears[action.year],
            data: action.data,
            loading: false,
          },
        },
      };

    case "SUBJECT_CHOICE_ERROR":
      return {
        ...state,
        subjectChoiceYears: {
          ...state.subjectChoiceYears,
          [action.year]: {
            ...state.subjectChoiceYears[action.year],
            error: action.data,
            loading: false,
          },
        },
      };

    default:
      return state;
  }
}
