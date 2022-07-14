function intersectionOfSortedArrays(array1, array2) {
    let arr1Dict = getFrequencyCountObject(array1);
    let arr2Dict = getFrequencyCountObject(array2);
    let newArr = []
    for ( let key of Object.keys(arr1Dict)){
        if(arr2Dict[key]){
            let w = 0;
            while( w < arr1Dict[key] && w < arr2Dict[key] ){
                newArr.push(key);
                w++;
            }
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