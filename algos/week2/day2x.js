function intersectionOfSortedArrays(array1, array2) {
    let arr1Dict = getFrequencyCountObject(array1);
    let arr2Dict = getFrequencyCountObject(array2);
    let newArr = []
    for ( let key of Object.keys(arr1Dict)){
        if(arr2Dict[key]){
            var x = Math.min(arr1Dict[key], arr2Dict[key]);
            newArr = newArr.concat(Array(x).fill(key));
        }
    }
    return newArr;
}

function getFrequencyCountObject(arr) {
    let frequencyCountObject = {};
    for ( let i = 0; i < arr.length; i++){
        if(frequencyCountObject[arr[i]]){
            frequencyCountObject[arr[i]]++;
        }else{
            frequencyCountObject[arr[i]] = 1;
        }
    }
    return frequencyCountObject;
}