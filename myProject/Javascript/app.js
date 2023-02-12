const a = 5;
const b = 2;
console.log("hihihihi");
console.log(a*b);

// 변하는 값일 경우에만 let 써주고 대부분 const 사용함
//array
const days = [
    "mon",
    "tue",
    "wed",
    "thu",
    "fri",
    "sat",
    "sun"
];

console.log(days);
console.log(days[3]);
days.push("Week"); //추가
console.log(days);
//object
const player = {
    name: "nico",
    handsom: false,
    points: 10,
}

console.log(player);
console.log(player.name);

player.name = "angela";
// const 지만 object명 자체의 변경이아닌 내부의 변경이라 가능 
player.LasteName = "potato";
console.log(player);

function Hello(name) {
    console.log("Hello my name is " + name);
}
console.log(Hello("nico"));

const calcu = {
    add: function (num1, num2) {
        console.log(num1 + num2);
    },

    div: function (num1, num2) {
        console.log(num1 / num2);
    },

    mul: function (num1, num2) {
        console.log(num1 * num2);
    },

    power: function (num1, num2) {
        console.log(num1 ** num2);
    }
}

calcu.add(2,3);
calcu.div(4,2);
calcu.mul(4,4);
calcu.power(2,4);




