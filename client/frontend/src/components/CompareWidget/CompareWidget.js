import Box from '@material-ui/core/Box';
import Divider from '@material-ui/core/Divider';
import FormControl from '@material-ui/core/FormControl';
import InputLabel from '@material-ui/core/InputLabel';
import ListSubheader from '@material-ui/core/ListSubheader';
import MenuItem from '@material-ui/core/MenuItem';
import Paper from '@material-ui/core/Paper';
import Select from '@material-ui/core/Select';
import React, { useCallback, useEffect, useMemo, useState } from 'react';
import { connect } from 'react-redux';
import { compareWidget } from '../../lib/redux/actions';
import { deepGet } from '../../lib/utils';
import { LineChart } from '../charts/LineChart';
import { COMPARE_STRUCTURE } from './config';
import { useChartSelectStyles, useStyles } from './styles';


const ChartSelect = ({ typeIndex, selectedUrls, setSelected, name, value }) => {
  const classes = useChartSelectStyles();

  const chartOptions = COMPARE_STRUCTURE[typeIndex].charts;

  const renderChartMenuItems = useCallback(() => chartOptions.map(({ type, label, name, url }, index) => {
    if (type === 'chart') {
      return <MenuItem key={ index } value={ url } disabled={ (selectedUrls || []).includes(url) }>{ label }</MenuItem>;
    } else if (type === 'delimiter') {
      return <ListSubheader key={ index }>{ label }</ListSubheader>;
    } else return <></>;
  }), [ chartOptions, selectedUrls ]);

  const labelId = useMemo(() => `${ name }-label`, [ name ]);
  return <Box className={ classes.box }>
    <FormControl className={ classes.formControl } variant="outlined">
      <InputLabel id={ labelId }>{ name }</InputLabel>
      <Select
        labelId={ labelId }
        value={ value }
        onChange={ (event => setSelected(deepGet(event, 'target.value', ''))) }
        label={ name }
      >
        { renderChartMenuItems() }
      </Select>
    </FormControl>
    <Divider/>
  </Box>;
};


const CompareWidget = ({ series1, series2, loadSeries1, loadSeries2, clearSeries }) => {
  const classes = useStyles();
  const compareTypes = useMemo(() => COMPARE_STRUCTURE.map(({ name }) => name), []);

  const [ selectedCompareType, setSelectedCompareType ] = useState(0);
  const [ selectedUrl1, setSelectedUrl1 ] = useState('');
  const [ selectedUrl2, setSelectedUrl2 ] = useState('');


  const onSelectedTypeChanged = useCallback(event => {
    clearSeries();
    setSelectedUrl1('');
    setSelectedUrl2('');
    setSelectedCompareType(event.target.value);
  }, [ clearSeries, setSelectedUrl1, setSelectedUrl2, setSelectedCompareType ]);

  const selectedUrls = useMemo(() => [ selectedUrl1, selectedUrl2 ].filter(value => !!value), [ selectedUrl1, selectedUrl2 ]);

  const renderCompareTypesMenuItems = useCallback(() => compareTypes.map((type, index) => (
    <MenuItem key={ type } value={ index }>{ type }</MenuItem>
  )), [ compareTypes ]);

  const typeUrl = useMemo(() => COMPARE_STRUCTURE[selectedCompareType].url, [ selectedCompareType ]);
  const urlPrefix = 'api/line-graphs';

  const url1 = useMemo(() => selectedUrl1 ? `${ urlPrefix }/${ typeUrl }/${ selectedUrl1 }` : undefined, [ typeUrl, selectedUrl1 ]);
  const url2 = useMemo(() => selectedUrl2 ? `${ urlPrefix }/${ typeUrl }/${ selectedUrl2 }` : undefined, [ typeUrl, selectedUrl2 ]);

  useEffect(() => {
    if (url1) loadSeries1(url1);
  }, [ url1, loadSeries1 ]);

  useEffect(() => {
    if (url2) loadSeries2(url2);
  }, [ url2, loadSeries2 ]);

  useEffect(() => {
    if (!url1 && !url2) {
      clearSeries();
      console.log('clear');
    }
  }, [ clearSeries, url1, url2 ]);

  const chartDataList = useMemo(() => [ series1, series2 ], [ series1, series2 ]);

  return <Paper className={ classes.paper }>
    { (url1 || url2) && <LineChart height={ 500 } chartDataList={ chartDataList }/> }
    <Box>
      <Box className={ classes.box }>
        <FormControl className={ classes.formControl } variant={ 'filled' } color={ 'primary' } size={ 'medium' }>
          <InputLabel>Tipul comparatiei</InputLabel>
          <Select
            value={ selectedCompareType }
            onChange={ onSelectedTypeChanged }
          >
            { renderCompareTypesMenuItems() }
          </Select>
        </FormControl>
      </Box>

      <ChartSelect name={ 'Prima serie' } typeIndex={ selectedCompareType } selectedUrls={ selectedUrls }
                   value={ selectedUrl1 }
                   setSelected={ setSelectedUrl1 }/>
      <ChartSelect name={ 'A doua serie' } typeIndex={ selectedCompareType } selectedUrls={ selectedUrls }
                   value={ selectedUrl2 }
                   setSelected={ setSelectedUrl2 }/>
    </Box>
  </Paper>;
};


const mapStateToProps = (state) => {
  return {
    series1: {
      data: state.compareWidget.series1,
      loading: state.compareWidget.series1Loading,
      errors: state.compareWidget.series1Error,
    },
    series2: {
      data: state.compareWidget.series2,
      loading: state.compareWidget.series2Loading,
      errors: state.compareWidget.series2Error,
    },
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    loadSeries1: (url) => {
      dispatch(compareWidget.loadSeries1(url));
    },
    loadSeries2: (url) => {
      dispatch(compareWidget.loadSeries2(url));
    },
    clearSeries: () => dispatch(compareWidget.clearSeries()),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(CompareWidget);

