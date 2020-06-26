import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { AboutUs, Dashboard, NotFound } from '../../../pages';
import { Others } from '../../../pages/Others';
import { Layout } from '../../Layout/Layout';

const RootContainer = () => {
  return (
    <BrowserRouter>
      <Layout>
        <Switch>
          <Route exact path="/">
            <Dashboard/>
          </Route>
          <Route exact path="/altele/">
            <Others/>
          </Route>
          <Route exact path="/aboutus">
            <AboutUs/>
          </Route>
          <Route>
            <NotFound/>
          </Route>
        </Switch>
      </Layout>
    </BrowserRouter>
  );
};

export default RootContainer;
