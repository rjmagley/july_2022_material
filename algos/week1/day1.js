function rotateArray(arr, shiftBy) {

    if (arr.length <= 1 || shiftBy === 0) {
        return arr;
    }

    // negative shift by values
    if (shiftBy < 0) {
        shiftBy = (shiftBy % arr.length) + arr.length;
    }


    for (var i = 0; i < shiftBy; i++) {
        var temp = arr.pop();
        arr.unshift(temp); 
    }

    // for (var i = 0; i < arr.length; i++) {
    //     var temp = arr[i];

    // }

    return arr;
}

console.log(rotateArray([1, 2, 3, 4, 5], 1))
console.log(rotateArray([1, 2, 3, 4, 5], -4))
console.log(rotateArray([1, 2, 3, 4, 5], 6))
console.log(rotateArray([1, 2, 3, 4, 5], -9))

console.log(rotateArray([1, 2, 3, 4, 5], 2))
// console.log(rotateArray([3, 7], 1))
// console.log(rotateArray([1, 2, 3, 4, 5], 3))
