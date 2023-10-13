const warriorsGames = [
  {
    awayTeam: {
      team: "Golden State",
      points: 119,
      isWinner: true,
    },
    homeTeam: {
      team: "Houston",
      points: 106,
      isWinner: false,
    },
  },
  {
    awayTeam: {
      team: "Golden State",
      points: 105,
      isWinner: false,
    },
    homeTeam: {
      team: "Houston",
      points: 127,
      isWinner: true,
    },
  },
  {
    homeTeam: {
      team: "Golden State",
      points: 126,
      isWinner: true,
    },
    awayTeam: {
      team: "Houston",
      points: 85,
      isWinner: false,
    },
  },
  {
    homeTeam: {
      team: "Golden State",
      points: 92,
      isWinner: false,
    },
    awayTeam: {
      team: "Houston",
      points: 95,
      isWinner: true,
    },
  },
  {
    awayTeam: {
      team: "Golden State",
      points: 94,
      isWinner: false,
    },
    homeTeam: {
      team: "Houston",
      points: 98,
      isWinner: true,
    },
  },
  {
    homeTeam: {
      team: "Golden State",
      points: 115,
      isWinner: true,
    },
    awayTeam: {
      team: "Houston",
      points: 86,
      isWinner: false,
    },
  },
  {
    awayTeam: {
      team: "Golden State",
      points: 101,
      isWinner: true,
    },
    homeTeam: {
      team: "Houston",
      points: 92,
      isWinner: false,
    },
  },
];

const makeChart = (gameData, targetTeam) => {
  const ul = document.createElement("ul");

  for (game of gameData) {
    const li = document.createElement("li");
    li.innerHTML = getScoreLine(game);
    li.classList.add(isWinner(game, targetTeam));
    ul.append(li);
  }
  return ul;
};

const getScoreLine = ({ homeTeam, awayTeam }) => {
  const teamNames = `${awayTeam.team} @ ${homeTeam.team} `;
  const { points: hPoints } = homeTeam;
  const { points: aPoints } = awayTeam;
  if (aPoints > hPoints) {
    return `${teamNames} <b>${awayTeam.points}</b> - ${homeTeam.points}`;
  }
  return `${teamNames} ${awayTeam.points} - <b>${homeTeam.points}</b>`;
};

const isWinner = ({ homeTeam, awayTeam }, targetTeam) => {
  const warriors = homeTeam.team === targetTeam ? homeTeam : awayTeam;
  return warriors.isWinner ? "win" : "loss";
};

const chart1 = makeChart(warriorsGames, "Golden State");
document.body.append(chart1);
