function deduplicateSortedArray(arr) {
    var dupes = 0;
    var temp;
    for (var i = 0; i < arr.length; i++) {
        console.log(arr);
        if (arr[i] === temp) {
            dupes++;
        } else {
            arr[i - dupes] = arr[i];
        }
        temp = arr[i];
    }
    arr.length -= dupes;
    return arr;
}