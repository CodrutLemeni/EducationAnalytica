import Box from "@material-ui/core/Box";
import React, { useEffect } from "react";
import { connect } from "react-redux";

const CountyPage = ({ loadCharts, countyHistogram }) => {
  useEffect(() => {
    loadCharts();
  }, [loadCharts]);
  // const history = useHistory();
  // const navigateToCountyDetails = useCallback((countyCode) => history.push(`/judete/${ countyCode }`), [ history ]);

  return <Box>You are seeing county list.</Box>;
};

const mapStateToProps = (state) => {
  return {
    countyHistogram: {
      data: state.globalStatistics.countyHistogram,
      loading: state.globalStatistics.countyHistogramLoading,
      errors: state.globalStatistics.countyHistogramErrors,
    },
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    loadCharts: () => {},
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(CountyPage);
