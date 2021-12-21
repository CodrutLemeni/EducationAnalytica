import React from "react";
import { Route, Switch, BrowserRouter } from "react-router-dom";
import {
  AboutUs,
  Dashboard,
  NotFound,
  GradeDistribList,
  GradeDistrib,
  SubChoiceList,
  SubChoice,
  GenderList,
  Gender,
  Maps,
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
            <GradeDistribList />
          </Route>
          <Route
            exact
            path="/grade-distrib/:subject"
            component={GradeDistrib}
          />

          <Route exact path="/sub-choice/">
            <SubChoiceList />
          </Route>
          <Route exact path="/sub-choice/:subject" component={SubChoice} />

          <Route exact path="/gender/">
            <GenderList />
          </Route>
          <Route exact path="/gender/:subject" component={Gender} />

          <Route exact path="/maps/">
            <Maps />
          </Route>

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
