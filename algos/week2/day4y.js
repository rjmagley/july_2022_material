function isAnagram(string_a, string_b) {
    return string_a.toUpperCase().split('').sort().join('')==string_b.toUpperCase().split('').sort().join('')
    
  }