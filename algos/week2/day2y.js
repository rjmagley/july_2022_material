function intersectionOfSortedArrays(array1, array2){
    var newarr = [];
    var i = 0, j = 0; 
    while(i < array1.length && j < array2.length){
        if (array1[i] == array2[j]){
            newarr.push(array1[i]);
            i++;
            j++;
        }
        else if (array1[i] < array2[j]){
            i++;
        }
        else {
            j++;
        }
    }

    return newarr;
}