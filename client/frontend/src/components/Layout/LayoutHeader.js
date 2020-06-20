import AppBar from '@material-ui/core/AppBar/AppBar';
import Box from '@material-ui/core/Box';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import clsx from 'clsx';
import React, { useCallback } from 'react';
import { Link, NavLink } from 'react-router-dom';
import { useLayoutHeaderStyle } from './styles';

const links = [
];

const CustomNavLink = ({ label, to, exact }) => {
  const classes = useLayoutHeaderStyle();

  return <NavLink
    exact={ exact }
    to={ to }
    className={ clsx(classes.link, classes.navLink) }
    activeClassName={ classes.navLinkActive }>
    <Typography className={ classes.navText } variant='body1'>
      { label }
    </Typography>
  </NavLink>;
};


const LayoutHeader = () => {
  const classes = useLayoutHeaderStyle();

  const renderAllLinks = useCallback(() => links.map((linkData, index) => <CustomNavLink { ...linkData }
                                                                                         key={ index }/>), []);

  return <AppBar position="static" className={ classes.appBar }>
    <Toolbar>
      <Link to='/' className={ classes.link }>
        <Typography className={ classes.inline } variant='h5'>EducationAnalytica </Typography>
      </Link>
      <Box className={ classes.flexExpander }/>
      { renderAllLinks() }
    </Toolbar>

  </AppBar>;
};

export default LayoutHeader;
