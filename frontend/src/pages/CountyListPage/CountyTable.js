import { TableHead } from '@material-ui/core';
import IconButton from '@material-ui/core/IconButton';
import Paper from '@material-ui/core/Paper';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableFooter from '@material-ui/core/TableFooter';
import TablePagination from '@material-ui/core/TablePagination';
import TableRow from '@material-ui/core/TableRow';
import DetailsIcon from '@material-ui/icons/Info';
import React, { useCallback, useMemo, useState } from 'react';
import { COUNTIES } from '../../config/countyInfo';
import { deepGet } from '../../lib/utils';
import { useCountyTableStyles } from './styles';

const ROWS_PER_PAGE = 10;


const CountyTable = ({ countyHistogram, onSelectCounty }) => {
  const countyListData = useMemo(() => deepGet(countyHistogram, 'data.content.data', []), [ countyHistogram ]);
  const sortedCountyListData = useMemo(() => countyListData.sort(({ value: value1 }, { value: value2 }) => value2 - value1), [ countyListData ]);
  const classes = useCountyTableStyles();

  const [ page, setPage ] = useState(0);
  const renderCountyList = useCallback(() => {
    return sortedCountyListData
      .slice(page * ROWS_PER_PAGE, (page + 1) * ROWS_PER_PAGE)
      .map(({ value, label }) => <TableRow
        key={ label }
        hover
      >
        <TableCell className={ classes.dataCell } align='left'>
          { COUNTIES[label] }
        </TableCell>
        <TableCell className={ classes.dataCell } align='left'>
          { value }
        </TableCell>
        <TableCell className={ classes.dataCell } align='left'>
          <IconButton onClick={ () => onSelectCounty(label) } size='small'>
            <DetailsIcon/>
          </IconButton>
        </TableCell>
      </TableRow>);
  }, [ sortedCountyListData, page, classes, onSelectCounty ]);

  return <Paper className={ classes.paper }>
    <TableContainer component={ Paper }>
      <Table className={ classes.table } size={ 'small' }>
        <TableHead className={ classes.tableHead }>
          <TableRow>
            <TableCell className={ classes.tableHeaderCell } align='left'>Județ</TableCell>
            <TableCell className={ classes.tableHeaderCell } align='left'>Nr. decese</TableCell>
            <TableCell className={ classes.tableHeaderCell } align='left'>Detalii</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          { renderCountyList() }
        </TableBody>
        <TableFooter>
          <TableRow>
            <TablePagination
              count={ countyListData.length }
              rowsPerPage={ ROWS_PER_PAGE }
              rowsPerPageOptions={ [ ROWS_PER_PAGE ] }
              page={ page }
              onChangePage={ (_, newPage) => setPage(newPage) }
            />
          </TableRow>
        </TableFooter>
      </Table>
    </TableContainer>
  </Paper>;
};

export default CountyTable;
