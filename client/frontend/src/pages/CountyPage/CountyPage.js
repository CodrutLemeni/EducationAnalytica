import Box from '@material-ui/core/Box';
import React, { useEffect } from 'react';
import { connect } from 'react-redux';
import { useParams } from 'react-router-dom';
import GradeDistributionChart from '../../components/charts/GradeDistributionChart/GradeDistributionChart';
import DeathDateChart from '../../components/charts/DeathDateChart/DeathDateChart';
import { GenderChart } from '../../components/charts/GenderChart';
import { withLayout } from '../../components/Layout';
import { countyStatistics } from '../../lib/redux/actions/';

const CountyPage = ({ loadCharts, ageHistogram, genderHistogram, deathDateHistogram }) => {
  const { countyCode } = useParams();
  console.log(countyCode);
  useEffect(() => {
    if (countyCode)
      loadCharts(countyCode);
  }, [ loadCharts, countyCode ]);

  return <Box>
    <GradeDistributionChart
      { ...ageHistogram }
      title={ 'Distribuția deceselor pe categorii de vârstă' }
      height={ 500 }
    />

    <GenderChart
      { ...genderHistogram }
      title={ 'Distribuția deceselor pe gen' }
      height={ 500 }
    />

    <DeathDateChart
      { ...deathDateHistogram }
      title={ 'Distribuția deceselor pe zile' }
      height={ 500 }
    />
  </Box>;
};

const mapStateToProps = state => {
  return {
    genderHistogram: {
      data: state.countyStatistics.genderHistogram,
      loading: state.countyStatistics.genderHistogramLoading,
      errors: state.countyStatistics.genderHistogramErrors,
    },
    ageHistogram: {
      data: state.countyStatistics.ageHistogram,
      loading: state.countyStatistics.ageHistogramLoading,
      errors: state.countyStatistics.ageHistogramErrors,
    },
    deathDateHistogram: {
      data: state.countyStatistics.deathDateHistogram,
      loading: state.countyStatistics.deathDateHistogramLoading,
      errors: state.countyStatistics.deathDateHistogramErrors,
    },
  };
};

const mapDispatchToProps = dispatch => {
  return {
    loadCharts: (countyCode) => {
      dispatch(countyStatistics.loadCountyHistograms(countyCode));
    },
  };
};


export default connect(mapStateToProps, mapDispatchToProps)(withLayout(CountyPage));

