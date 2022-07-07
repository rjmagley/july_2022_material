function deduplicateSortedArray(arr){
    if (arr.length <= 1){
        return arr;
    }
    var prev = 0;
    for (var i = 1; i < arr.length; i++){
        if (arr[i] != arr[prev]){
            prev++;
            arr[prev] = arr[i]
        }
        console.log(arr);
    }
    arr.length = prev + 1;
    return arr
}

deduplicateSortedArray([0,0,0,0,1,1,1,2,3,3,3,3,3,3,4,4,4,5,6,6,6,6,7,7,9,11,11,14,16,16,16])