import { createMuiTheme } from '@material-ui/core';

export default createMuiTheme({
  palette: {
    primary: {
      light: '#87dfd6',
      main: '#01a9b4',
      dark: '#086972',
      contrastText: '#ffffff',
    },
    secondary: {
      light: '#fafdb2',
      main: '#fbfd8a',
      dark: '#fdde85',
      contrastText: '#111111',
    },
    layout: {
      logoutIcon: '#ff6659',
    },
  },
  typography: {},
});
