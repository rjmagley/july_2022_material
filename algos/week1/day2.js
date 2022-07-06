/**
 * @param arr is a list<int>
 * @returns int
 */
 export function arrayBalanceIndex(arr) {
  
    // left-right checking with i as a fulcrum
    for(var i = 0; i < arr.length; i++){
      // initiates/resets sum values
      var sumLeft = 0;
      var sumRight = 0;
  
      // loop summing of values left and right
      for(var j = 0; j < arr.length; j++){
        // sums values greater and less than i
        if(j < i){
          sumLeft += arr[j]
       }
        else if(j > i){
          sumRight += arr[j]
        }
      }
      // comparator - checks left vs right, returns i if values are equal
      if(sumLeft == sumRight){
        return i;
      }
    }
    // if value not found, return -1
    return -1
  }