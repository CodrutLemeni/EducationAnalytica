import AppBar from "@material-ui/core/AppBar/AppBar";
import Box from "@material-ui/core/Box";
import Divider from "@material-ui/core/Divider";
import IconButton from "@material-ui/core/IconButton";
import Drawer from "@material-ui/core/Drawer";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemText from "@material-ui/core/ListItem";
import Tab from "@material-ui/core/Tab";
import Tabs from "@material-ui/core/Tabs";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import MenuOpen from "@material-ui/icons/MenuOpen";
import React from "react";
import { withGetScreen } from "react-getscreen";
import { Link, useHistory } from "react-router-dom";
import { useLayoutHeaderStyle } from "./styles";
import logo_text from "../../images/logo_text.png";
import logo_styled from "../../images/logo_styled.png";

const links = [
  { label: "Home", to: "" },
  { label: "Distributia notelor", to: "grade-distrib" },
  { label: "Alegera subiectului III", to: "sub-choice" },
  { label: "Fete vs Baieti", to: "gender" },
  { label: "Alte", to: "altele" },
  { label: "Despre noi", to: "aboutus" },
];

const getSelectedFromUlr = (location) => {
  let value = -1;
  links.forEach((linkData, index) => {
    if (linkData.to === location.split("/")[1]) value = index;
  });
  return value;
};

const LayoutHeader = ({ isMobile }) => {
  const [selected, setSelected] = React.useState(
    getSelectedFromUlr(window.location.pathname)
  );
  const [drawerOpen, setDrawerOpen] = React.useState(false);

  const history = useHistory();

  const classes = useLayoutHeaderStyle();

  const renderAllLinks = () => {
    if (isMobile()) return renderDrawer();
    return renderFullMenu();
  };

  const renderDrawer = () => (
    <>
      <IconButton
        aria-label="more"
        aria-controls="long-menu"
        aria-haspopup="true"
        onClick={() => {
          setDrawerOpen(true);
        }}
      >
        <MenuOpen color="secondary" fontSize="large" />
      </IconButton>
      <Drawer
        anchor="right"
        open={drawerOpen}
        onClose={() => setDrawerOpen(false)}
        PaperProps={{
          className: classes.drawer,
        }}
      >
        <List>
          {links.map((linkData, index) => (
            <>
              <ListItem
                button
                key={index}
                onClick={() => {
                  history.push("/" + linkData.to);
                  setDrawerOpen(false);
                }}
              >
                <ListItemText>
                  <Typography
                    align="center"
                    variant="h6"
                    className={classes.dropDownItemText}
                  >
                    {linkData.label}
                  </Typography>
                </ListItemText>
              </ListItem>

              {index !== links.length - 1 ? <Divider /> : null}
            </>
          ))}
        </List>
        <img
          src={logo_styled}
          alt="Logo"
          className={classes.drawerLogo}
          onClick={() => {
            history.push("/");
            setDrawerOpen(false);
          }}
        />
      </Drawer>
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
            history.push("/" + linkData.to);
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
          <img src={logo_text} alt="Logo" className={classes.logo} />
        </Link>

        <Box className={classes.flexExpander} />
        {renderAllLinks(selected, setSelected, history)}
      </Toolbar>
    </AppBar>
  );
};

export default withGetScreen(LayoutHeader);
