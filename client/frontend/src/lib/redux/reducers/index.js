import { combineReducers } from "redux";
import globalStatistics from "./globalStatistics";
import countyStatistics from "./countyStatistics";
import genericStatistics from "./genericStatistics";
import compareWidget from "./compareWidget";
import subjectChoice from "./subjectChoice";
import gradeDistribution from "./gradeDistribution";
import gender from "./gender";

export const rootReducer = combineReducers({
  globalStatistics,
  countyStatistics,
  genericStatistics,
  compareWidget,
  subjectChoice,
  gradeDistribution,
  gender,
});
