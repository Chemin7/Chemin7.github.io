let longestString = (str) =>{
    let result = ""

    for (let letter of str){
        if(!result.includes(letter))
            result+=letter
            
    }

    return result
}

console.log(longestString('aaaabbbbcccaaabbcccaaert'))