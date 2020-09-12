const checkNonDecreasing = number => {
    const str = String(number);
    for (let i = 1; i < str.length; ++i) {
        if (Number(str[i]) < Number(str[i - 1])) {
            return false;
        }
    }
    return true;
};

const checkDouble = number => {
    const str = String(number);
    let check = false;
    for (let i = 1; i < str.length - 2; ++i) {
        if (str[i] === str[i+1] && str[i] !== str[i-1] && str[i+1] !== str[i+2]){
            check = true;
            break;
        }
    }
    return check || (str[0] === str[1] && str[1] != str[2]) || (str[str.length - 1] === str[str.length-2] && str[str.length-2] !== str[str.length-3]);
};

const range = (start, end) => {
    const array = [];
    for (let i = start; i <= end; ++i) {
        array.push(i);
    }
    return array;
};

const number = range(245182, 790572).filter(number => checkNonDecreasing(number) && checkDouble(number));

console.log(number, number.length);