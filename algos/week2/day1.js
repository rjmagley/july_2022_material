function arrayOddOccurances(arr){
    var values = {};

    for (var i=0; i < arr.length; i++){
        if (values[arr[i]] != undefined){
            values[arr[i]]++;
        }
        else {
            values[arr[i]] = 1;
        }
    }

    for (var j in values){
        if(values[j] % 2 == 1){
            return j;
        }
    } 

    return values
}