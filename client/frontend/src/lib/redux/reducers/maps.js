const initialSate = {
  maps: {},
};

export default function maps(state = initialSate, action) {
  switch (action.type) {
    case "MAP_LOADING":
      return {
        ...state,
        maps: {
          ...state.maps,
          [action.year]: {
            ...state.maps[action.year],
            loading: true,
          },
        },
      };

    case "MAP_LOADED":
      return {
        ...state,
        maps: {
          ...state.maps,
          [action.year]: {
            ...state.maps[action.year],
            data: {
              ...action.data,
              meta: {
                ...action.data.meta,
                title: `Media pe judete in anul ${action.year}`,
              },
            },
            loading: false,
          },
        },
      };

    case "MAP_ERROR":
      return {
        ...state,
        maps: {
          ...state.maps,
          [action.year]: {
            ...state.maps[action.year],
            error: action.data,
            loading: false,
          },
        },
      };

    default:
      return state;
  }
}
