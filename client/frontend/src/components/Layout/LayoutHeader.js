import AppBar from "@material-ui/core/AppBar/AppBar";
import Box from "@material-ui/core/Box";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import Tab from "@material-ui/core/Tab";
import Tabs from "@material-ui/core/Tabs";
import IconButton from "@material-ui/core/IconButton";
import Menu from "@material-ui/core/Menu";
import MenuItem from "@material-ui/core/MenuItem";
import MoreVertIcon from "@material-ui/icons/MoreVert";
import { withGetScreen } from "react-getscreen";
import React, { useCallback } from "react";
import { useHistory, Link } from "react-router-dom";
import { useLayoutHeaderStyle } from "./styles";

const links = [
  { label: "Home", to: "" },
  { label: "Alte", to: "altele" },
  { label: "Despre noi", to: "aboutus" },
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
            maxHeight: 48 * 4.5,
            width: "20ch",
          },
        }}
      >
        {links.map((linkData, index) => (
          <MenuItem
            key={index}
            selected={false}
            onClick={() => {
              history.push(linkData.to);
              setAnchorEl(null);
            }}
          >
            {linkData.label}
          </MenuItem>
        ))}
      </Menu>
    </>
  );

  const renderFullMenu = () => (
    <Tabs
      centered
      value={selected}
      onChange={(event, newValue) => {
        setSelected(newValue);
      }}
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
        <Typography className={classes.inline} variant="h5">
          EducationAnalytica{" "}
        </Typography>

        <Box className={classes.flexExpander} />
        {renderAllLinks(selected, setSelected, history)}
      </Toolbar>
    </AppBar>
  );
};

export default withGetScreen(LayoutHeader);
