// const age = +prompt("Enter your age: ");
// toHundred = 100 - age;
// console.log(`You will turn 100 in ${toHundred} years.`);


// const radius = +prompt("Enter the radius: ");
// const areaofCircle = Math.PI * radius ** 2;
// console.log(`Area of circle is ${areaofCircle.toFixed(2)}`);

const name = "Tusar";
function reverseFunc(name) {
    let nametoArr = name.split("");
    let newArr = [];
    for (let i = nametoArr.length; i > 0; i--) {
        newArr.push(nametoArr[i-1])
    }

    let reverse = newArr.join("");
    console.log(reverse);
    
}

reverseFunc("Rakibul Islam");