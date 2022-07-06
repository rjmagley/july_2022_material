function arrayBalanceIndex(arr) {
    if (arr.length <= 1) {
        return -1
    }

    var left = 0;
    var right = 0;

    for (var j = 1; j < arr.length; j++) {
        right += arr[j];
    }

    for (var i = 0; i < arr.length; i++) {
        if (left == right) {
            return i
        }
        right -= arr[i + 1]
        left += arr[i]
    }

    return -1;
}

// [3, 4, 9, 2, 4, -2, 3]