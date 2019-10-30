// This is where you implement your solution 
const convertCoordinates = (agents) => {
  if ( agents.length === 0) {
    return [];
  }

  return agents.map((alphaNumber) => {
    return [
      letterToNumber(alphaNumber.slice(0,1)),
      parseInt(alphaNumber.slice(1)) - 1
    ];
  });
}

const findSafePlaces = (agents) => {
  let places = [], savePlaces = [], maxDistance = 1;
  for (i = 0; i < 10; i++) {
    for (j = 0; j < 10; j++) {
      places.push([i, j]);
    }
  }

  places.forEach((place) => {
    const min = getSmalestDistance(place, agents);
    
    if (maxDistance < min) {
      savePlaces = [];
      savePlaces.push(place);

      maxDistance = min;
    } else if (maxDistance === min) {
      savePlaces.push(place);
    }
  });

  return savePlaces;
}

const adviceForAda = (agents) => {
  const agentCoordinates = convertCoordinates(agents);

  const validAgents = validateAgents(agentCoordinates);
  if (validAgents.length === 0) {
    return 'The whole city is safe for Ada! :-)';
  }

  const savePlaces = findSafePlaces(validAgents);
  if (savePlaces.length === 0) {
    return 'There are no safe locations for Ada! :-('
  }
  return savePlaces.map(coordinatesToString);
}

module.exports = {
  convertCoordinates,
  findSafePlaces,
  adviceForAda
}

// Helper functions
const letterPosition = [
  'A', 'B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J'
]

function letterToNumber(letter) {
  return letterPosition.findIndex((position) => letter === position);
}

function coordinatesToString([x, y]) {
  return letterPosition[x] + (y + 1);
}

function validateAgents(agents) {
  return agents.filter(([x, y]) => {
    return 0 <= x && x <= 9 &&
           0 <= y && y <= 9;
  });
}

function getSmalestDistance(place, agents) {
  let min = 100;

  agents.forEach((agent) => {
    const x = Math.abs(agent[0] - place[0]); 
    const y = Math.abs(agent[1] - place[1]);
    const distance = x + y;

    if (min > distance) {
      min = distance
    }
  })

  return min;
}
