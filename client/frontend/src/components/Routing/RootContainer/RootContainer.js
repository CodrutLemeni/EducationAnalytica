import React from "react";
import { Route, Switch, BrowserRouter } from "react-router-dom";
import {
  AboutUs,
  Dashboard,
  NotFound,
  GradeDistrib,
  SubChoiceList,
  SubChoice,
} from "../../../pages";
import { Others } from "../../../pages/Others";
import { Layout } from "../../Layout/Layout";

const RootContainer = () => {
  return (
    <BrowserRouter>
      <Layout>
        <Switch>
          <Route exact path="/">
            <Dashboard />
          </Route>
          <Route exact path="/grade-distrib/">
            <GradeDistrib />
          </Route>
          <Route exact path="/sub-choice/">
            <SubChoiceList />
          </Route>
          <Route exact path="/sub-choice/:subject" component={SubChoice} />
          <Route exact path="/altele/">
            <Others />
          </Route>
          <Route exact path="/aboutus">
            <AboutUs />
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
