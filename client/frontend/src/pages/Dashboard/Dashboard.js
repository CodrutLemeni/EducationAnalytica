import Box from "@material-ui/core/Box";
import Grid from "@material-ui/core/Grid";
import React, { useEffect } from "react";
import { connect } from "react-redux";
import { ArticleBox } from "../../components/ArticleBox";
import Chart from "../../components/charts/Chart/Chart";
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
          <TitleBox title={"Cateva lucruri despre Bacalaureat 2019"}>
            <p>
              În acest grafic se poate observa distribuția notelor pentru toate
              notele din fiecare probă. Important de constatat este multitudinea
              notelor de 5 obținute față de celelalte note, fiind cea mai
              populară notă. S-au obținut aproape de 10 ori mai multe note de
              trecere față de nota 4. O altă importantă caracteristică este
              numărul mare de note de 10. Aceasta este doua cea mai intâlnită
              notă, numărul de apariții fiind însă doar putin peste jumătate din
              numărul de apariții de nota 5.
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
          <ArticleBox title={"Procentajul de promovabilitate"}>
            <p>
              În 2019, 70.9% dintre fete au promovat examenul de bacalaureat în
              comparație cu doar 59.5% dintre băieți. Tendința ca un procentaj
              mai mare al fetelor sa treac bacalaureatul comparat cu cel al
              baietilor se poate observa inclusiv pentru fiecare profil (vezi
              graficul de mai jos). Pentru profilul de matematică-informatică,
              care este și unul dintre profilele cu cea mai mare
              promovabilitate, diferenta dintre băieți și fete se află în jurul
              valorii de 5%. Pentru profilul de filologie, diferența crește la
              10%, iar pentru celelalte profile decât cele menționate,
              procentajul ajunge la mai mult de 13%.
            </p>
          </ArticleBox>
        </Grid>

        <Grid item xs={12} md={6}>
          <ArticleBox title={"Procentajul de promovabilitate pe judete"}>
            <p>
              În harta de mai jos, sunt reprezentate media tuturor notelor
              obtinute a studenților care au avut notă de trecere per fiecare
              judet în anul 2019. Judetele cu un indice mai mare corespund unei
              culori mai intunecate. Astfel, se poate observa ca județele Brașov
              și Olt se afla la fruntea clasamentului, iar Mehedinti, Suceava
              sau Maramureș au o medie per judet mai mica decât toate celelalte
              județe. Pozitia de județ fruntaș in educatie al judetului Brașov
              este dat si de numărul ridicat de persoane care au trecut
              bacaleauratul (72,74%) față de media țării de 69.1%.
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
