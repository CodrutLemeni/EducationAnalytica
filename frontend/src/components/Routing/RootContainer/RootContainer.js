import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { NotFound, Dashboard, CountyDetailPage, CountyListPage } from '../../../pages';

const RootContainer = () => {
  return (
    <BrowserRouter>
      <Switch>
        <Route exact path="/">
          <Dashboard/>
        </Route>
        <Route exact path="/judete/">
          <CountyListPage/>
        </Route>
        <Route exact path="/judete/:countyCode">
          <CountyDetailPage/>
        </Route>
        <Route>
          <NotFound/>
        </Route>
      </Switch>
    </BrowserRouter>
  );
};

export default RootContainer;
