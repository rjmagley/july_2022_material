export function deduplicateSortedArray(arr) {

    for (var i = 0; i < arr.length; i++) {
      while (arr[i] == arr[i + 1]) {
        arr.splice(i + 1, 1);
      }
    }
  
    return arr;
  }