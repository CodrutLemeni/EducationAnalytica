import AppBar from '@material-ui/core/AppBar/AppBar';
import Box from '@material-ui/core/Box';
import Divider from '@material-ui/core/Divider';
import IconButton from '@material-ui/core/IconButton';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';
import Tab from '@material-ui/core/Tab';
import Tabs from '@material-ui/core/Tabs';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import MoreVertIcon from '@material-ui/icons/MoreVert';
import React from 'react';
import { withGetScreen } from 'react-getscreen';
import { Link, useHistory } from 'react-router-dom';
import { useLayoutHeaderStyle } from './styles';

const links = [
  { label: "Home", to: "" },
  { label: "Alte", to: "altele" },
  { label: "Despre noi", to: "aboutus" },
  { label: "Judete", to: "judete" },
  { label: "Judete", to: "judete" },
  { label: "Judete", to: "judete" },
  { label: "Judete", to: "judete" },
  { label: "Judete", to: "judete" },
];

const getSelectedFromUlr = (location) => {
  let value = -1;
  links.forEach((linkData, index) => {
    if ("/" + linkData.to === location) value = index;
  });
  return value;
};

const LayoutHeader = (props) => {
  const [selected, setSelected] = React.useState(
    getSelectedFromUlr(window.location.pathname)
  );

  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);

  const history = useHistory();

  const classes = useLayoutHeaderStyle();

  const renderAllLinks = () => {
    if (props.isMobile()) return renderDropdownMenu();
    return renderFullMenu();
  };

  const renderDropdownMenu = () => (
    <>
      <IconButton
        aria-label="more"
        aria-controls="long-menu"
        aria-haspopup="true"
        onClick={(event) => {
          setAnchorEl(event.currentTarget);
        }}
      >
        <MoreVertIcon />
      </IconButton>
      <Menu
        id="long-menu"
        anchorEl={anchorEl}
        keepMounted
        open={open}
        onClose={() => setAnchorEl(null)}
        PaperProps={{
          style: {
            width: "20ch",
          },
        }}
      >
        {links.map((linkData, index) => (
          <>
            <MenuItem
              key={index}
              selected={index === selected}
              onClick={() => {
                history.push(linkData.to);
                setAnchorEl(null);
              }}
            >
              <Typography
                align="center"
                variant="h6"
                className={classes.dropDownItemText}
              >
                {linkData.label}
              </Typography>
            </MenuItem>
            {index !== links.length - 1 ? <Divider /> : null}
          </>
        ))}
      </Menu>
    </>
  );

  const renderFullMenu = () => (
    <Tabs

      value={selected}
      onChange={(event, newValue) => {
        setSelected(newValue);
      }}
      variant="scrollable"
      scrollButtons="auto"
    >
      {links.map((linkData, index) => (
        <Tab
          label={linkData.label}
          key={index}
          value={index}
          onClick={(event) => {
            history.push(linkData.to);
          }}
          className={classes.tab}
        />
      ))}
    </Tabs>
  );

  return (
    <AppBar position="static" className={classes.appBar}>
      <Toolbar>
        <Link to="/" className={classes.link} onClick={() => setSelected(0)}>
          <Typography className={classes.inline} variant="h5">
            EducationAnalytica
          </Typography>
        </Link>

        <Box className={classes.flexExpander} />
        {renderAllLinks(selected, setSelected, history)}
      </Toolbar>
    </AppBar>
  );
};

export default withGetScreen(LayoutHeader);
