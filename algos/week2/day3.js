function bookIndex(pages) {
    var stringArray = [];
    var output = "";

    for (var i = 0; i < pages.length; i++) {
        if (pages[i] + 1 != pages[i + 1]) {
            stringArray.push(String(pages[i]));
        }
        else {
            let leftPage = pages[i];
            while (pages[i] + 1 == pages[i + 1]) {
                i++;
            }
            let rightPage = pages[i];

            stringArray.push(`${leftPage}-${rightPage}`)
        }
    }

    // output = stringArray.join(', ')

    for (var i = 0; i < stringArray.length; i++) {
        output += stringArray[i];
        if (i != stringArray.length - 1) {
            output += ', ';
        }
    }

    return output;
}