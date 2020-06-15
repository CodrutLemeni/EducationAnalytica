import Box from '@material-ui/core/Box';
import Grid from '@material-ui/core/Grid';
import React, { useEffect } from 'react';
import { connect } from 'react-redux';
import Chart from '../../components/charts/Chart/Chart';
import { withLayout } from '../../components/Layout';
import { globalStatistics } from '../../lib/redux/actions/';

const Dashboard = ({ loadCharts, gradeDistExample, averageGradeDistExample }) => {
  useEffect(() => loadCharts(), [ loadCharts ]);

  return <Box>
    <Grid container>
      <Grid item xs={ 12 } md={ 7 }>

      </Grid>
      <Grid item xs={ 12 } md={ 5 }>
      </Grid>
    </Grid>

    <Chart height={ 500 } chartData={ gradeDistExample }/>
    <Chart height={ 500 } chartData={ averageGradeDistExample }/>
  </Box>;
};

const mapStateToProps = state => {
  return {
    gradeDistExample: {
      data: state.globalStatistics.gradeDistribution,
      loading: state.globalStatistics.gradeDistributionLoading,
      errors: state.globalStatistics.gradeDistributionErrors,
    },
    averageGradeDistExample: {
      data: state.globalStatistics.averageGradePerProfileDistribution,
      loading: state.globalStatistics.averageGradePerProfileDistributionLoading,
      errors: state.globalStatistics.averageGradePerProfileDistributionErrors,
    },
  };
};

const mapDispatchToProps = dispatch => {
  return {
    loadCharts: () => {
      dispatch(globalStatistics.loadGlobalHistograms());
    },
  };
};


export default connect(mapStateToProps, mapDispatchToProps)(withLayout(Dashboard));

