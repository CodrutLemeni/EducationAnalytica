import { Typography } from "@material-ui/core";

import Box from "@material-ui/core/Box";
import Grid from "@material-ui/core/Grid";
import React from "react";

import logo from "./logo.png";

import { useStyles } from "./styles";

export default function AboutUs() {
  const styles = useStyles();

  return (
    <>
      <Box className={styles.topBox}>
        <Typography variant={"h4"} className={styles.title}>
          Noi Suntem <span className={styles.titleName}>EduAnalytica</span>
        </Typography>
        <Typography variant={"h5"} className={styles.subtitle}>
          Facem o diferenta prin informare
        </Typography>

        <Grid container className={styles.imageGrid}>
          <Grid item xs={6}>
            <img src={logo} className={styles.logo} alt={"logo"} />
          </Grid>
          <Grid item xs={6}>
            <Typography variant="h5" className={styles.text}>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut sed
              sollicitudin lacus. <br />
              <br />
              Etiam quis sagittis nisl. In hac habitasse platea dictumst.
              Suspendisse ultricies neque ac risus accumsan ultrices.
              Suspendisse potenti. <br />
              <br />
              Nam ultrices vel ipsum sit amet iaculis. Cras ultrices est id est
              convallis malesuada. Nulla quis semper lacus. Quisque viverra eu
              turpis sed commodo.
            </Typography>
          </Grid>
        </Grid>
      </Box>

      <Box className={styles.goalsBox}>
        <Typography variant={"h4"} className={styles.title}>
          <span className={styles.titleName}>Tintele</span> noastre
        </Typography>
      </Box>
    </>
  );
}
