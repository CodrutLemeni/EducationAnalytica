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
    } catch (err) {
      return { data: null, err };
    }
  };

  return {
    getHBC,
  };
};
