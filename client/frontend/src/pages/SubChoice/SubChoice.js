import React, { useEffect } from "react";

import { NotFound } from "../";

import { Chart } from "../../components/charts/Chart";
import { TitleBox } from "../../components/TitleBox";
import { Box, Grid, Typography } from "@material-ui/core";

import { connect } from "react-redux";
import { loadSubjectChoiceForSubject } from "../../lib/redux/actions/subjectChoice";
/** Params may be:
 *  filologie, mate-info, resurse-naturale, profil-tehnic, stiinte ale naturii
 */

const subjects = [
  {
    id: 0,
    label: "Filologie",
    code: "filologie",
    options:
      "Geografie, Logică şi argumentare, Psihologie, Economie, Sociologie, Filosofie",
    text: (
      <>
        Majoritatea eleviilor care au terminat <strong>filologia</strong>{" "}
        preferă geografia în toți anii considerați. Este important de observat,
        însă, că procentajul elevilor care aleg această opțiune este în scădere
        acelerată din 2015, an în care acest procentaj se afla la valoarea de
        aproximativ 67%, până în 2019, când valoarea a ajuns la 52.8%. În
        același timp, preferința pentru logică aproape s-a dublat. În 2015, 17%
        dintre elevii de la filologie au ales această opțiune, procentaj care a
        ajuns la aproximativ 31% în 2019.
      </>
    ),
  },
  {
    id: 1,
    label: "Matematica Informatica",
    code: "mate-info",
    options: "Fizică, Chimie, Biologie, Informatică",
    text: (
      <>
        Pentru profilul de <strong>matematică-informatică</strong>, optiunea
        principală în perioada 2015-2019 a fost anatomia, procentajul de elevi
        care aleg această opțiune fiind în jurul valorii de 36%. O creștere în
        popularitate se poate observa pentru opțiunile de informatică, care a
        crescut de la 19.2% în 2015 din alegerile elevilor la 26.9% în 2019,
        respectiv fizică care a ajuns opțiunea de bacalaureat pentru 21.5%
        dintre elevi relativ cu valoarea de 14.3% în 2015. Aceste creșteri au
        fost, în mare parte, în detrimentul biologiei de clasele a IX-a și a X-a
        care a scăzut constant în această perioadă, ajungând ca în 2019, nici
        10% dintre elevi să prefere această alternativă.
      </>
    ),
  },
  {
    id: 2,
    label: "Stiinte ale Naturii",
    code: "stiinte-ale-naturii",
    options: "Fizică, Chimie, Biologie, Informatică",
    text: (
      <>
        Alegerea anatomiei ca proba a III-a la bacalaureat reprezintă opțiunea
        majoritară pentru elevii de la <strong>științe ale naturii</strong>.
        Această opțiune se află într-o continua creștere în perioada 2015-2019,
        întrucât procentajul de 62.8% dintre elevi care au ales această probă în
        2015 a ajuns la 68.4% în 2019. Opțiunile de fizică și informatică se
        află într-o creștere ușoară. Un trend descendent se poate observa pentru
        opțiunea biologiei de clasele a IX-a si a X-a, care a scăzut de la 18.7%
        în 2015 la 10.3% în 2019.
      </>
    ),
  },
  {
    id: 3,
    label: "Profil Tehnic",
    code: "profil-tehnic",
    options: "Fizică, Chimie, Biologie",
    text: (
      <>
        Pentru profilul <strong>tehnic</strong>, alegerea biologiei de clasele
        IX-X pentru proba a III-a este de departe cea mai populară opțiune. Mai
        mult, față de anul 2015, se observa o ușoara creștere în procentajul de
        elevi care preferă biologia în 2019. A doua opțiune a elevilor de la
        profilul tehnic o reprezintă fizica. Procentajul elevilor care au ales
        această opțiune în perioada 2015-2019 a fost aproximativ 10%, valoarea
        cunoscând puține variații.
      </>
    ),
  },
  {
    id: 4,
    label: "Profil Resurse naturale şi protecţia mediului",
    code: "profil-resurse-naturale",
    options: "Fizică, Chimie, Biologie",
    text: (
      <>
        La profilul de <strong>resurse naturale și protecția mediului</strong>,
        opțiunile clar majoritare sunt reprezentate de anatomie și biologie.
        Acestea constituie, în mod constant, mai mult de 92% dintre opțiunile
        elevilor de la acest profil. Analizând în detaliu aceste alegeri, se
        poate observa că anatomia crește în popularitate, crescând cu
        aproximativ 14 procente din 2015 până în 2019, în detrimentul biologiei,
        care scăzut de la 46% la 35% în aceeași perioadă.
      </>
    ),
  },
];

const SubChoice = ({ match, subjectChoiceYears, loadCharts }) => {
  const { label, options, code, text } = subjects.find(
    (sub) => sub.code === match.params.subject
  );
  useEffect(() => loadCharts(code), [loadCharts]);

  if (label === undefined) return <NotFound />;

  return (
    <Box>
      <TitleBox title={label}>{text}</TitleBox>
      <Grid container spacing={5}>
        {Object.entries(subjectChoiceYears).map(([key, value], index) => (
          <Grid item xs={12} md={6} key={index}>
            <Chart height={500} chartData={value} />
          </Grid>
        ))}
      </Grid>
    </Box>
  );
};

const mapStateToProps = (state) => {
  return {
    subjectChoiceYears: state.subjectChoice.subjectChoiceYears,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    loadCharts: (subject) => {
      dispatch(loadSubjectChoiceForSubject(subject));
    },
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(SubChoice);
