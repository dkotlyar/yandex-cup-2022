let translator = (numbers) => {
    const obj = {
        ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_0123456789: null
    }
    let alphabet = null
    for (let k in obj) {
        alphabet = k
    }
    let space = {}.toString().at(7)
    let underscore = alphabet.at(52)
    alphabet = alphabet.slice(53) + alphabet.slice(0, 52) + space

    let empty = alphabet.slice(0, 0)

    return numbers.map(n => n >= 0 && n < alphabet.length ? alphabet.at(n) : underscore).join(empty)
}

module.exports = translator

console.log(translator([14,12,22,10,28,38,53,44,51,55,62,2,0,1,5]))
console.log(translator([17,40,47,47,50,62,34,36,12,56,51,62,2,0,2,2]))
console.log(translator([17,40,47,47,50,62,32,50,53,47,39,-1, 70]))

// console.log('A')