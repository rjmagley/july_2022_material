function isAnagram(string_a, string_b) {
    // any way to return false? maybe not
    var string_a_modified = string_a.toUpperCase();
    var string_b_modified = string_b.toUpperCase();

    var string_a_object = {}; 

    for (var i = 0; i < string_a_modified.length; i++) {
        // char - short for character
        let char = string_a_modified[i];
        if (char == ' ') {
            continue;
        }
        if (string_a_object[char] == undefined) {
            string_a_object[char] = 1;
        }
        else {
            string_a_object[char] += 1;
        }
    }

    var string_b_object = {}; 

    for (var i = 0; i < string_b_modified.length; i++) {
        // char - short for character
        let char = string_b_modified[i];
        if (char == ' ') {
            continue;
        }
        if (string_b_object[char] == undefined) {
            string_b_object[char] = 1;
        }
        else {
            string_b_object[char] += 1;
        }
    }

    // we have the count of characters for each string
    // now we can compare and see if they are/are not anagrams

    // return string_a_object == string_b_object;
    // can't do this - can't compare equality of objects like this

    var string_a_keys = Object.keys(string_a_object);
    var string_b_keys = Object.keys(string_b_object);

    for (var i = 0; i < string_a_keys.length; i++) {
        let key = string_a_keys[i];
        if (string_a_object[key] != string_b_object[key]) {
            return false;
        }
    }

    for (var i = 0; i < string_b_keys.length; i++) {
        let key = string_b_keys[i];
        if (string_b_object[key] != string_a_object[key]) {
            return false;
        }
    }

    return true;
}