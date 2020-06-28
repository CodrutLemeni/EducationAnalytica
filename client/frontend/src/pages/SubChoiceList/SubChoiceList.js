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
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed suscipit
          aliquet ultricies. Orci varius natoque penatibus et magnis dis
          parturient montes, nascetur ridiculus mus. Duis faucibus purus ac
          justo dictum, quis finibus purus dignissim. Morbi venenatis non elit
          eget tincidunt. In quis dapibus orci, sit amet pretium turpis.
          Curabitur malesuada, magna vitae mattis pellentesque, ligula arcu
          sodales odio, quis consequat elit magna posuere nisl. Nam scelerisque
          dui a luctus faucibus. Curabitur vestibulum orci vitae imperdiet
          commodo.
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
