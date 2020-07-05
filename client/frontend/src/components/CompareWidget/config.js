export const COMPARE_STRUCTURE = [
  {
    name: 'După promovabilitate',
    min: 0,
    max: 100,
    url: 'evolutie-promovabilitate',
    charts: [
      {
        type: 'chart',
        label: 'Evolutia promovabilitatii la mate-info',

        url: 'mate-info',
      },
      {
        type: 'chart',
        label: 'Evolutia promovabilitatii la filologie',

        url: 'filologie',
      },
      {
        type: 'chart',
        label: 'Evolutia promovabilitatii la stiinte ale naturii',

        url: 'stiinte-ale-naturii',
      },
      {
        type: 'chart',
        label: 'Evolutia promovabilitatii la stiinte sociale',

        url: 'stiinte-sociale',
      },
      {
        type: 'chart',
        label: 'Evolutia promovabilitatii la filiera tehnologica si tehnica',

        url: 'filiera-tehnologica-si-tehnica',
      },
      {
        type: 'chart',
        label: 'Evolutia promovabilitatii in zona urbana',

        url: 'zona-urbana',
      },
      {
        type: 'chart',
        label: 'Evolutia promovabilitatii in zona rurala',

        url: 'zona-rurala',
      },
    ],
  },
  {
    name: 'După alegere subiectul 3',
    min: 0,
    max: 100,
    url: 'procentaj-alegere-s3',
    charts: [
      {
        type: 'delimiter',
        label: 'Mate-Info',
      },
      {
        type: 'chart',
        label: 'Procentaj alegere informatica - Mate info',

        url: 'mate-info/informatica',
      },
      {
        type: 'chart',
        label: 'Procentaj alegere fizica - Mate info',

        url: 'mate-info/fizica',
      },
      {
        type: 'delimiter',
        label: 'Stiinte ale naturii',
      },
      {
        type: 'chart',
        label: 'Procentaj alegere informatica - Stiinte ale naturii',

        url: 'stiinte-ale-naturii/informatica',
      },
      {
        type: 'chart',
        label: 'Procentaj alegere fizica - Stiinte ale naturii',

        url: 'stiinte-ale-naturii/fizica',
      },
    ],
  },
  {
    name: 'Dupa medie',
    min: 0,
    max: 10,
    url: 'evolutie-medie',
    charts: [
      {
        type: 'chart',
        label: 'Media filiera tehnologica si tehnica',
        url: 'filiera-tehnologica-si-tehnica',
      },
      {
        type: 'chart',
        label: 'Filologie',
        url: 'filologie',
      },
      {
        type: 'chart',
        label: 'Mate info',
        url: 'mate-info',
      },
      {
        type: 'chart',
        label: 'Stiinte ale naturii',
        url: 'stiinte-ale-naturii',
      },
      {
        type: 'chart',
        label: 'Stiinte sociale',
        url: 'stiinte-sociale',
      },
      {
        type: 'chart',
        label: 'Total',
        url: 'total',
      },
      {
        type: 'chart',
        label: 'Zona rurala',
        url: 'zona-rurala',
      },
      {
        type: 'chart',
        label: 'Zona urbana',
        url: 'zona-urbana',
      },
    ],
  },
];