import CssBaseline from '@material-ui/core/CssBaseline';
import { ThemeProvider } from '@material-ui/core/styles';
import echarts from 'echarts';
import moment from 'moment';
import MuiPickersUtilsProvider from '@material-ui/pickers/MuiPickersUtilsProvider';
import React from 'react';
import { Provider } from 'react-redux';
import { applyMiddleware, createStore } from 'redux';
import thunk from 'redux-thunk';
import RootContainer from './components/Routing/RootContainer/RootContainer';
import { rootReducer } from './lib/redux/reducers';
import theme from './lib/theme';
import MomentUtils from '@date-io/moment';
import geoJson from './config/romania_map';

moment.locale('ro');

let store = createStore(rootReducer, applyMiddleware(thunk));

echarts.registerMap('RO', geoJson);


function App() {
  return (
    <>
    <CssBaseline/>
    <ThemeProvider theme={ theme }>
      <MuiPickersUtilsProvider utils={ MomentUtils }>
        <Provider store={ store }>
          <RootContainer/>
        </Provider>
      </MuiPickersUtilsProvider>
    </ThemeProvider>
  </>
  );
}

export default App;
