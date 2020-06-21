import { Container } from "@material-ui/core";
import Box from "@material-ui/core/Box";
import React from "react";
import LayoutHeader from "./LayoutHeader";
import { useStyles } from "./styles";

export const Layout = ({ children }) => {
  const classes = useStyles();
  return (
    <Box className={classes.root}>
      <LayoutHeader />
      <Container className={classes.container}>{children}</Container>
    </Box>
  );
};

export const withLayout = (PageComponent) => {
  return (props) => {
    return (
      <Layout>
        <PageComponent {...props} />
      </Layout>
    );
  };
};
