import Box from '@material-ui/core/Box';
import React, { useEffect } from 'react';
import { connect } from 'react-redux';
import { CompareWidget } from '../../components/CompareWidget';
import { genericStatistics } from '../../lib/redux/actions/';

const chartsToLoad = {
  'ala': '/api/grade-distributions/2015',
  'bala': '/api/grade-distributions/2016',
};

const Others = ({ loadCharts, charts }) => {
  useEffect(() => loadCharts(chartsToLoad), [ loadCharts ]);
  return (
    <Box>
      <CompareWidget/>
    </Box>
  );
};

const mapStateToProps = (state) => {
  return {
    charts: state.genericStatistics,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    loadCharts: (props) => {
      dispatch(genericStatistics.loadGenericStatistics(props));
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(Others);
