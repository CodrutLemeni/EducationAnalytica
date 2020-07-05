import React from "react";
import { useHistory } from "react-router-dom";
import { useStyles } from "./styles";

import { TitleBox } from "../../components/TitleBox";
import {
  Box,
  Card,
  CardContent,
  Typography,
  Grid,
  CardActionArea,
} from "@material-ui/core";

const subjects = [
  {
    id: 0,
    label: "Filologie",
    code: "filologie",
    options:
      "Geografie, Logică şi argumentare, Psihologie, Economie, Sociologie, Filosofie",
  },
  {
    id: 1,
    label: "Matematica Informatica",
    code: "mate-info",
    options: "Fizică, Chimie, Biologie, Informatică",
  },
  {
    id: 2,
    label: "Stiinte ale Naturii",
    code: "stiinte-ale-naturii",
    options: "Fizică, Chimie, Biologie, Informatică",
  },
  {
    id: 3,
    label: "Profil Tehnic",
    code: "profil-tehnic",
    options: "Fizică, Chimie, Biologie",
  },
  {
    id: 4,
    label: "Profil Resurse naturale şi protecţia mediului",
    code: "profil-resurse-naturale",
    options: "Fizică, Chimie, Biologie",
  },
];

const SubChoiceList = ({}) => {
  const classes = useStyles();
  const history = useHistory();

  const handleClick = (code) => () => {
    history.push(`/sub-choice/${code}`);
  };

  return (
    <Box>
      <TitleBox title={"Alegerea subiectului III"}>
        <p>
          Pentru profilul de matematică-informatică, optiunea principală in
          perioada 2015-2019 a fost Anatomia, procentajul de elevi care aleg
          această opțiune fiind in jurul valorii de 36%. O creștere în
          popularitate se poate observa pentru opțiunile de informatică, care a
          crescut de la 19.2% in 2015 din alegerile elevilor la 26.9% in 2019,
          respectiv fizică care a ajuns optiunea de bacalaureat pentru 21.5%
          dintre elevi relativ cu valoarea de 14.3% în 2015. Aceste creșteri au
          fost, în mare parte, în detrimentul biologiei de clasa a IX-a si a X-a
          care a scăzut constant în această perioadă, ajungând ca în 2019, nici
          10% dintre elevi să prefere această alternativă.
          <br />
          <br />
          Pentru profilul tehnic, alegerea biologiei de clasele IX-X pentru
          proba a III-a este de departe cea mai populară opțiune. Mai mult, față
          de anul 2015, se observă o ușoara creștere în procentajul de elevi
          care preferă biologia în 2019. A doua opțiune a elevilor de la
          profilul tehnic o reprezintă fizică. Procentajul elevilor care au ales
          această opțiune în perioada 2015-2019 a fost aproximativ 10%, valoarea
          cunoscând puține variații.
        </p>
      </TitleBox>
      <Grid container spacing={5}>
        {subjects.map((sub) => (
          <Grid
            item
            xs={12}
            md={6}
            lg={3}
            className={classes.cell}
            key={sub.id}
          >
            <Card className={classes.card}>
              <CardActionArea onClick={handleClick(sub.code)}>
                <CardContent>
                  <Typography
                    className={classes.title}
                    color="textSecondary"
                    gutterBottom
                  >
                    Profil
                  </Typography>
                  <Typography variant="h5" component="h2">
                    {sub.label}
                  </Typography>
                  <Typography variant="body2" component="p">
                    Optiuni: {sub.options}
                  </Typography>
                </CardContent>
              </CardActionArea>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Box>
  );
};

export default SubChoiceList;
