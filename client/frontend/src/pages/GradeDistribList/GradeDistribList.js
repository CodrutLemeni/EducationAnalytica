import React from "react";
import { useHistory } from "react-router-dom";

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
    label: "General",
    code: "general",
    options: "Toate materiile",
  },
];

function GradeDistribList() {
  const history = useHistory();

  const handleClick = (code) => () => {
    history.push(`/grade-distrib/${code}`);
  };

  return (
    <Box>
      <TitleBox title={"Distribtia notelor"}>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam maximus vel
        enim quis lacinia. Pellentesque gravida tellus tincidunt velit vehicula
        tempus. Nullam sit amet cursus lacus. Morbi augue ex, fringilla non
        suscipit eget, scelerisque semper ipsum. Nulla facilisi. Nam eget quam
        in tortor consequat ultricies. In hac habitasse platea dictumst. Fusce
        sollicitudin auctor ultrices. Sed venenatis, dolor non dictum dapibus,
        justo libero fringilla purus, id malesuada diam urna vel purus. Fusce
        elementum lorem eget porta rhoncus. Cras sodales enim et libero lacinia
        mollis. Nunc semper euismod enim. Curabitur enim lacus, facilisis eget
        risus eget, dignissim lacinia erat. Fusce a lacus efficitur erat
        fringilla tristique ac aliquam dui. Praesent porttitor ex sem, id tempor
        nulla sodales in.
      </TitleBox>
      <Grid container spacing={5}>
        {subjects.map((sub) => (
          <Grid item xs={12} md={6} lg={3} key={sub.id}>
            <Card>
              <CardActionArea onClick={handleClick(sub.code)}>
                <CardContent>
                  <Typography color="textSecondary" gutterBottom>
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
}

export default GradeDistribList;
