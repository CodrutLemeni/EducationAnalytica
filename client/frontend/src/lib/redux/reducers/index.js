import { combineReducers } from 'redux';
import globalStatistics from './globalStatistics';
import countyStatistics from './countyStatistics';

export const rootReducer = combineReducers({
  globalStatistics, countyStatistics
});

