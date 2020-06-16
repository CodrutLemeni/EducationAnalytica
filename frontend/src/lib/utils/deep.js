export function deepGet(obj, property, defaultValue) {
  if (!obj) return defaultValue;

  if (/\./g.test(property)) {
    const properties = property.split('.');
    return deepGet(obj[properties[0]], properties.slice(1).join('.'), defaultValue);
  } else {
    return [ undefined, null ].indexOf(obj[property]) === -1 ? obj[property] : defaultValue;
  }
}

export function deepSet(obj, property, value) {
  if (/\./g.test(property)) {
    const properties = property.split('.');
    if (!obj[properties[0]]) {
      obj[properties[0]] = {};
    }
    deepSet(obj[properties[0]], properties.slice(1).join('.'), value);
  } else {
    obj[property] = value;
  }
}