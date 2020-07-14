/**
 * Loads jsons from folders
 * Db is just a name, this is not really a database
 */
exports.initDb = ({ config }, callback) => {
  const db = createDb(config);
  callback({ config, db });
};

createDb = (config) => {
  const getHBC = ({ subfolder, year }) => {
    try {
      const data = require(`../data/${config.hbc_root}/${subfolder}/${year}.json`);
      return { data, error: null };
    } catch (error) {
      return { data: null, error };
    }
  };

  const getGradeDistrib = ({ year, subfolder }) => {
    try {
      const data = require(`../data/${config.grade_distrib_root}/${subfolder}/${year}.json`);
      return { data, error: null };
    } catch (error) {
      return { data: null, error };
    }
  };

  const getMapChart = ({ year }) => {
    try {
      const data = require(`../data/${config.map_chart_root}/${year}.json`);
      return { data, error: null };
    } catch (error) {
      return { data: null, error };
    }
  };

  const getLineChart = ({ subfolder, section, area }) => {
    console.log({ subfolder, section, area });
    if (section === undefined) section = ".";
    try {
      const data = require(`../data/${config.lc_root}/${subfolder}/${section}/${area}.json`);
      return { data, error: null };
    } catch (error) {
      return { data: null, error };
    }
  };

  return {
    getHBC,
    getGradeDistrib,
    getMapChart,
    getLineChart,
  };
};
