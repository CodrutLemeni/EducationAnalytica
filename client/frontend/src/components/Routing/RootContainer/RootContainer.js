import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import {
  NotFound,
  Dashboard,
  CountyDetailPage,
  CountyListPage,
} from "../../../pages";
import { Layout } from "../../Layout/Layout";

const RootContainer = () => {
  return (
    <BrowserRouter>
      <Layout>
        <Switch>
          <Route exact path="/">
            <Dashboard />
          </Route>
          <Route exact path="/judete/">
            <CountyListPage />
          </Route>
          <Route exact path="/judete/:countyCode">
            <CountyDetailPage />
          </Route>
          <Route>
            <NotFound />
          </Route>
        </Switch>
      </Layout>
    </BrowserRouter>
  );
};

export default RootContainer;
