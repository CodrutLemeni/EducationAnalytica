import Divider from '@material-ui/core/Divider';
import FormControl from '@material-ui/core/FormControl';
import InputLabel from '@material-ui/core/InputLabel';
import ListSubheader from '@material-ui/core/ListSubheader';
import MenuItem from '@material-ui/core/MenuItem';
import Paper from '@material-ui/core/Paper';
import Select from '@material-ui/core/Select';
import React, { useCallback, useMemo, useState } from 'react';
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

  return <Paper className={ classes.paper }>
    <FormControl className={ classes.formControl }>
      <InputLabel>{ name }</InputLabel>
      <Select
        value={ value }
        onChange={ (event => setSelected(event.target.value)) }
      >
        { renderChartMenuItems() }
      </Select>
    </FormControl>
    <Divider/>
  </Paper>;
};


const CompareWidget = () => {
  const classes = useStyles();
  const compareTypes = useMemo(() => COMPARE_STRUCTURE.map(({ name }) => name), []);

  const [ selectedCompareType, setSelectedCompareType ] = useState(0);

  const [ selectedUrl1, setSelectedUrl1 ] = useState('');
  const [ selectedUrl2, setSelectedUrl2 ] = useState('');


  const renderCompareTypesMenuItems = useCallback(() => compareTypes.map((type, index) => (
    <MenuItem key={ type } value={ index }>{ type }</MenuItem>
  )), [ compareTypes ]);


  return <Paper className={ classes.paper }>
    <FormControl className={ classes.formControl }>
      <InputLabel htmlFor="grouped-select">Tipul comparatiei</InputLabel>
      <Select
        id="grouped-select"
        value={ selectedCompareType }
        onChange={ (event => setSelectedCompareType(event.target.value)) }>
        { renderCompareTypesMenuItems() }
      </Select>
    </FormControl>
    <Divider/>
    <ChartSelect id={ 'first' } typeIndex={ selectedCompareType } selectedUrls={ [] } value={ selectedUrl1 }
                 setSelected={ setSelectedUrl1 }/>
    <ChartSelect id={ 'second' } typeIndex={ selectedCompareType } selectedUrls={ [] } value={ selectedUrl2 }
                 setSelected={ setSelectedUrl2 }/>

  </Paper>;
};

export default CompareWidget;