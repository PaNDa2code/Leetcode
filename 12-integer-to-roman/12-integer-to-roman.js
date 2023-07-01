/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
  const arab = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
  const roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'];
  let i = 0;
  let out = '';

  for(i in arab){
    if(num>=arab[i]){
      out += roman[i].repeat(Math.floor(num/arab[i]))
      num %= arab[i]
    }
  }

  return out
}