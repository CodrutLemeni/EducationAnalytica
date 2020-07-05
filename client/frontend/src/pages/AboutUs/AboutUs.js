import { Typography } from "@material-ui/core";

import Box from "@material-ui/core/Box";
import Grid from "@material-ui/core/Grid";
import Divider from "@material-ui/core/Divider";
import React from "react";

import logo from "../../images/logo_emblem.png";

import { useStyles } from "./styles";
import clsx from "clsx";

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
          <Grid item xs={12} md={6}>
            <img src={logo} className={styles.logo} alt={"logo"} />
          </Grid>
          <Grid item xs={12} md={6}>
            <Typography variant="h5" className={styles.text}>
              <Typography variant="inherit" className={styles.contrastText}>
                Cine?
              </Typography>
              <br />
              Education Analytica este un ONG ce are ca scop detectarea și
              soluționarea actualelor probleme ale sistemului de învățământ din
              România, pentru eficientizarea metodelor de predare și evaluare
              ale elevilor.
            </Typography>
          </Grid>
        </Grid>
      </Box>

      <Grid container>
        <Grid item xs={12} md={6}>
          <Typography variant="h5" className={styles.text}>
            <Typography variant="inherit" className={styles.contrastText}>
              Cum?
            </Typography>
            <br />
            În momentul de față, multe țări folosesc data science în procesele
            de decizie, deoarece constituie unul dintre domeniile care au un
            impact semnificativ în îmbunătățirea viitorului, prin obiectivitate
            și corectitudine. Astfel, prin analiza minuțioasă a informațiilor
            referitoare la rezultatele elevilor în cadrul evenimentelor cheie
            anuale din trecut, înțelegerea situației actuale preia o formă mai
            clară, punctele slabe sunt identificate precis, iar procesul de
            îmbunătățire începe din timp, fiind modelat în concordanță cu
            nevoile.
          </Typography>
        </Grid>
        <Divider />
        <Grid item xs={12} md={6}>
          <Typography variant="h5" className={styles.text}>
            <Typography variant="inherit" className={styles.contrastText}>
              De ce?
            </Typography>
            <br />
            Pentru că educația reprezintă fundamentul formării personale,
            punctul de start la care ar trebui să aibă acces fiecare individ.
            Sistemul de învățământ trebuie sa fie accesibil, riguros și adaptat
            atât nevoilor în continuă schimbare ale societății, cât și
            diferențelor de background socio-economic.
          </Typography>
        </Grid>
      </Grid>
    </>
  );
}
