export const keysToCamel = function (o) {
  if (isObject(o)) {
    const n = {};
    Object.keys(o).forEach((k) => {
        n[toCamel(k)] = keysToCamel(o[k]);
      });
    return n;
  } else if (isArray(o)) {
    return o.map((i) => {
      return keysToCamel(i);
    });
  }
  return o;
};

export const keysToUnderscore = function (o) {
  if (isObject(o)) {
    const n = {};
    Object.keys(o)
      .forEach((k) => {
        n[toUnderscore(k)] = keysToUnderscore(o[k]);
      });
    return n;
  } else if (isArray(o)) {
    return o.map((i) => {
      return keysToUnderscore(i);
    });
  }
  return o;
};

const isArray = function (a) {
  return Array.isArray(a);
};

const toCamel = (s) => {
  return s.replace(/([-_][a-z])/ig, ($1) => {
    return $1.toUpperCase().replace('_', '');
  });
};

const toUnderscore = (s) => {
  return s.replace(/([A-Z])/g, ($1) => {
    return `_${ $1.toLowerCase() }`;
  });
};

const isObject = function (o) {
  return o === Object(o) && !isArray(o) && typeof o !== 'function';
};
