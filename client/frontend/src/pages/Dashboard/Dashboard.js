import Box from "@material-ui/core/Box";
import Grid from "@material-ui/core/Grid";
import React, { useEffect } from "react";
import { connect } from "react-redux";
import { ArticleBox } from "../../components/ArticleBox";
import Chart from "../../components/charts/Chart/Chart";
import { withLayout } from "../../components/Layout";
import { TitleBox } from "../../components/TitleBox";
import { globalStatistics } from "../../lib/redux/actions/";

const Dashboard = ({
  loadCharts,
  gradeDistExample,
  averageGradeDistExample,
  countyGradeDistExample,
}) => {
  useEffect(() => loadCharts(), [loadCharts]);

  return (
    <Box>
      <Grid container>
        <Grid item xs={12}>
          <TitleBox title={"Titlu mare si tare"}>
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed
              suscipit aliquet ultricies. Orci varius natoque penatibus et
              magnis dis parturient montes, nascetur ridiculus mus. Duis
              faucibus purus ac justo dictum, quis finibus purus dignissim.
              Morbi venenatis non elit eget tincidunt. In quis dapibus orci, sit
              amet pretium turpis. Curabitur malesuada, magna vitae mattis
              pellentesque, ligula arcu sodales odio, quis consequat elit magna
              posuere nisl. Nam scelerisque dui a luctus faucibus. Curabitur
              vestibulum orci vitae imperdiet commodo.
            </p>
          </TitleBox>
        </Grid>
        <Grid item xs={12}>
          <Chart height={500} chartData={gradeDistExample} />
        </Grid>
        <Grid item xs={12} md={6}>
          <Chart height={500} chartData={averageGradeDistExample} />
        </Grid>
        <Grid item xs={12} md={6}>
          <ArticleBox title={"Titlu articol"}>
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed
              suscipit aliquet ultricies. Orci varius natoque penatibus et
              magnis dis parturient montes, nascetur ridiculus mus. Duis
              faucibus purus ac justo dictum, quis finibus purus dignissim.
              Morbi venenatis non elit eget tincidunt. In quis dapibus orci, sit
              amet pretium turpis. Curabitur malesuada, magna vitae mattis
              pellentesque, ligula arcu sodales odio, quis consequat elit magna
              posuere nisl. Nam scelerisque dui a luctus faucibus. Curabitur
              vestibulum orci vitae imperdiet commodo.
            </p>
            <p>
              Vestibulum posuere erat quam, eget iaculis libero porta ut.
              Pellentesque habitant morbi tristique senectus et netus et
              malesuada fames ac turpis egestas. Sed quis dui eu velit egestas
              blandit vel a nunc. Lorem ipsum dolor sit amet, consectetur
              adipiscing elit. Aliquam pellentesque sodales lorem eget
              venenatis.
            </p>
            <p>
              Vestibulum posuere erat quam, eget iaculis libero porta ut.
              Pellentesque habitant morbi tristique senectus et netus et
              malesuada fames ac turpis egestas. Sed quis dui eu velit egestas
              blandit vel a nunc. Lorem ipsum dolor sit amet, consectetur
              adipiscing elit. Aliquam pellentesque sodales lorem eget
              venenatis.
            </p>
          </ArticleBox>
        </Grid>

        <Grid item xs={12} md={6}>
          <ArticleBox title={"Titlu articol"}>
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed
              suscipit aliquet ultricies. Orci varius natoque penatibus et
              magnis dis parturient montes, nascetur ridiculus mus. Duis
              faucibus purus ac justo dictum, quis finibus purus dignissim.
              Morbi venenatis non elit eget tincidunt. In quis dapibus orci, sit
              amet pretium turpis. Curabitur malesuada, magna vitae mattis
              pellentesque, ligula arcu sodales odio, quis consequat elit magna
              posuere nisl. Nam scelerisque dui a luctus faucibus. Curabitur
              vestibulum orci vitae imperdiet commodo.
            </p>
            <p>
              Vestibulum posuere erat quam, eget iaculis libero porta ut.
              Pellentesque habitant morbi tristique senectus et netus et
              malesuada fames ac turpis egestas. Sed quis dui eu velit egestas
              blandit vel a nunc. Lorem ipsum dolor sit amet, consectetur
              adipiscing elit. Aliquam pellentesque sodales lorem eget
              venenatis.
            </p>
          </ArticleBox>
        </Grid>
        <Grid item xs={12} md={6}>
          <Chart height={500} chartData={countyGradeDistExample} />
        </Grid>
      </Grid>
    </Box>
  );
};

const mapStateToProps = (state) => {
  return {
    gradeDistExample: {
      data: state.globalStatistics.gradeDistribution,
      loading: state.globalStatistics.gradeDistributionLoading,
      errors: state.globalStatistics.gradeDistributionErrors,
    },
    averageGradeDistExample: {
      data: state.globalStatistics.averageGradePerProfileDistribution,
      loading: state.globalStatistics.averageGradePerProfileDistributionLoading,
      errors: state.globalStatistics.averageGradePerProfileDistributionErrors,
    },
    countyGradeDistExample: {
      data: state.globalStatistics.averageGradePerCountyDistribution,
      loading: state.globalStatistics.averageGradePerCountyDistributionLoading,
      errors: state.globalStatistics.averageGradePerCountyDistributionErrors,
    },
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    loadCharts: () => {
      dispatch(globalStatistics.loadGlobalHistograms());
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(Dashboard);
