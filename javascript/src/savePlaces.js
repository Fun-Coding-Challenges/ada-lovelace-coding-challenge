const convertCoordinates = (agents) => {
  if (typeof agents !== 'undefined' && agents.length > 0)
  {
    let coordinates =[];
    for( let i = 0; i < agents.length; i++){
      coordinates.push([xCoord.indexOf(agents[i].charAt(0)), getYCoord(agents[i])]);
    }
    return coordinates
  }
  return []
}

const findSafePlaces = (agents) => {

  let places = [], safePlaces = [], max = 0;
  for (let i = 0; i < 10; i++)
    for (let j = 0; j < 10; j++)
      places.push([i,j]);

  for (let i = 0; i < places.length; i++)
  {
      min = 100;
      for (let j = 0; j < agents.length; j++)
      {
          let difference = [agents[j][0] - places[i][0], agents[j][1] - places[i][1]]
          let sum = Math.abs(difference[0]) + Math.abs(difference[1]);
          if (sum < min) 
            min = sum;
      }
      if (max == min)
      {
        safePlaces.push(places[i])
      }
      if (max < min)
      {
        max = min;
        safePlaces = [];
        safePlaces.push(places[i]); 
      } 
  }
  if (max != 0)
    return safePlaces;

  return []; 

}

const adviceForAda = (agents) => {
  let agentFound = false;
  if (typeof agents !== 'undefined' && agents.length > 0)
  {
    for (let i = 0; i < agents.length; i++){
      if (xCoord.indexOf(agents[i].charAt(0))>=0 && getYCoord(agents[i]) <= 9 ){
        agentFound = true;
      }
    }
    if (!agentFound){
      return 'The whole city is safe for Ada! :-)';
    }

    let places = findSafePlaces(convertCoordinates(agents));

    if (places.length > 0)
    {
      let safePlaces = [];
      for(let i = 0; i < places.length; i++)
      {
         //let x = xCoord[places[i][0]];
         //let y = places[i][1] + 1;
         //safePlaces.push(x.concat(y));    
         
         safePlaces.push(xCoord[places[i][0]].concat(places[i][1] + 1));
      }    
      return safePlaces;
    }
  }
  if (agentFound == true)
    return 'There are no safe locations for Ada! :-(';
  return 'The whole city is safe for Ada! :-)';
}

module.exports = {
  convertCoordinates,
  findSafePlaces,
  adviceForAda
}

const xCoord = ["A","B","C","D","E","F","G","H","I","J"];

function getYCoord(element){
  return parseInt(element.slice(1, element.length)) - 1
}
