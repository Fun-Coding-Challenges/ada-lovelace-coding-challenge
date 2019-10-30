// This is where you implement your solution 
const convertCoordinates = (agents) => {
  if ( !agents || agents.length === 0) {
    return [];
  }

  return agents.map((alphaNumber) => {
    coordinates = [];
    coordinates[0] = letterToNumber(alphaNumber.slice(0,1));
    coordinates[1] = parseInt(alphaNumber.slice(1)) - 1;
    return coordinates;
  });
}

const findSafePlaces = (agents) => {
  let places = [], savePlaces = [], maxDistance = 0;
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
    } else if (maxDistance == min) {
      savePlaces.push(place);
    }
  });

  return savePlaces;
}

const adviceForAda = (agents) => {
  return "adviceForAda"
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