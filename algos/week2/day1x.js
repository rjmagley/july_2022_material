function arrayOddOccurances(arr) {
    let numTracker = {};
    for ( let i = 0; i < arr.length; i++){
      if(numTracker[arr[i]]){
        delete numTracker[arr[i]];
      } else {
        numTracker[arr[i]] = 1;
      }
    }
    for(let key of Object.keys(numTracker)){
      return key;
    }
  }