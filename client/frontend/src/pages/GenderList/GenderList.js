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
    label: "Fete vs Baieti",
    code: "fete-baieti",
    options: "",
  },
  {
    id: 1,
    label: "Fete vs baieti mate-info, filologie, stiinte ale naturii",
    code: "fete-baieti-mate-info-filo-si-stiinte",
    options: "",
  },
  {
    id: 2,
    label: "Procentaj promovabilitate fete vs baieti urban si rural",
    code: "procentaj-promovabilitate-fete-baieti-urban-rural",
    options: "",
  },
  {
    id: 3,
    label: "Procentaj alegere profil in functie de sex",
    code: "procentaj-alegere-profil-in-functie-de-sex",
  },
];

function GenderList() {
  const history = useHistory();

  const handleClick = (code) => () => {
    history.push(`/gender/${code}`);
  };

  return (
    <Box>
      <TitleBox title={"Fete vs Baieti"}>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed facilisis
          tortor eros, id finibus ligula vehicula luctus. Nullam molestie, diam
          nec tristique congue, libero nisi fermentum metus, eu dignissim magna
          enim eu ante. Nullam euismod odio velit, a placerat turpis convallis
          in. In hac habitasse platea dictumst. Etiam ut tempor urna, rhoncus
          sagittis enim. Mauris congue vehicula feugiat. Integer congue commodo
          velit, ut laoreet nisi fermentum ut. Mauris lacus justo, lobortis eu
          purus sit amet, faucibus dignissim mi. Fusce gravida hendrerit nisi,
          vulputate luctus libero rhoncus eu. Sed purus massa, efficitur id
          aliquam vitae, eleifend at elit.
          <br />
          <br />
          Praesent augue urna, rhoncus ullamcorper erat et, convallis gravida
          mauris. Nullam nunc erat, feugiat id purus in, accumsan tincidunt
          diam. Pellentesque sed neque sed nisi porta auctor. Class aptent
          taciti sociosqu ad litora torquent per conubia nostra, per inceptos
          himenaeos. Vivamus tincidunt vehicula elit sed sodales. Nulla in augue
          non nunc feugiat tempus sodales sed felis. Proin fermentum, nisi ac
          dapibus faucibus, elit ante mattis leo, in molestie felis ante a
          velit. Duis laoreet non odio sollicitudin sollicitudin.
        </p>
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
                    {sub.options}
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

export default GenderList;
