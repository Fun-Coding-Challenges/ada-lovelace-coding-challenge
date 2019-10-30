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
  return "findSafePlaces"
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
