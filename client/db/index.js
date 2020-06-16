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

  const getGradeDistrib = ({ year }) => {
    try {
      const data = require(`../data/${config.grade_distrib_root}/${year}.json`);
      return { data, error: null };
    } catch (error) {
      return { data: null, error };
    }
  };

  const getMapChart = ({ year }) => {
    try {
      const data = require(`../data/${config.map_chart_root}/${year}.json`);
      return { data, error: null };
    } catch (err) {
      return { data: null, error };
    }
  };

  return {
    getHBC,
    getGradeDistrib,
    getMapChart,
  };
};
