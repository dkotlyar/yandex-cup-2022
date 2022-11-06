let lint = (text, tokensMap, rules) => {
    let specialChar = '.'
    let tokensList = []
    let lintText = text.split('').map(char => specialChar).join('')

    // console.log(lintText)

    for (let k in tokensMap) {
        let noToken = false
        let tokenValue = tokensMap[k]
        if (k[0] === '-') {
            k = k.split('').slice(1).join('')
            noToken = true
        }
        let index = text.indexOf(k)
        while (index > -1) {
            let replacement = tokenValue
            if (noToken) {
                text = text.slice(0, index) + replacement + text.slice(index + k.length)
                lintText = lintText.slice(0, index) + replacement + lintText.slice(index + k.length)
            } else {
                if (tokensList.indexOf(replacement) === -1) {
                    tokensList.push(replacement)
                    replacement = 'let ' + replacement
                }
                let textReplacement = replacement.split('').map(char => specialChar).join('')
                text = text.slice(0, index) + textReplacement + text.slice(index + k.length)
                lintText = lintText.slice(0, index) + replacement + lintText.slice(index + k.length)
            }
            index = text.indexOf(k)
        }
    }

    let replaceCount = 0
    do {
        replaceCount = 0
        for (let k in rules) {
            let index = text.indexOf(k)
            while (index > -1) {
                let replacement = rules[k].toString()
                text = text.slice(0, index) + replacement + text.slice(index + k.length)
                lintText = lintText.slice(0, index) + replacement + lintText.slice(index + k.length)
                index = text.indexOf(k)
                replaceCount++
            }
        }
    } while (replaceCount === 0)

    text.split('').forEach((char, index) => {
        if (char !== specialChar) {
            lintText = lintText.slice(0, index) + char + lintText.slice(index + char.length)
        }
    })

    return lintText
}

module.exports = lint

const rulesMap = {
    "t": 1,
    "l": "s",
    "s": 3,
    "d": 4,
    "k": 9,
    "*": "\n",
}
const tokensMap = {
    "ab": "val1",
    "cd": "val2",
    "ef": "val3",
    "-d": "k",
}
// let text = 'lg=lv_ll_lg=vl'
// text = text.slice(0, index) + k + text.slice(index + k.length)
// text = text.slice(0, 0) + 'val' + text.slice(2)
// console.log(text)
console.log(lint('ab=tl*cd=ls*ef=dd', tokensMap, rulesMap))