function rotateArray(arr, shiftBy) {

    if (arr.length == 0) {
        return arr;
    }

    // needs to handle negative shiftBy values - i.e. shifting to the left
    shiftBy = shiftBy % arr.length;

    if (shiftBy < 0) {
        shiftBy = shiftBy + arr.length;
    }

    var newArr = [];

    for (var i = 0; i < arr.length; i++) {
        x = ((arr.length + i - shiftBy) % arr.length)
        newArr.push(arr[x])
    }

    arr.length = 0;
    
    for (var i = 0; i < newArr.length; i++) {
        arr.push(newArr[i]);
    }
 
    return arr;
}

console.log(rotateArray([1, 2, 3, 4, 5], 1))
console.log(rotateArray([1, 2, 3, 4, 5], -4))
console.log(rotateArray([1, 2, 3, 4, 5], 6))
console.log(rotateArray([1, 2, 3, 4, 5], -9))

console.log(rotateArray([1, 2, 3, 4, 5], 2))