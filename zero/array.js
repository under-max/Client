'use strict'
//Q1 make a string out of an array
{
    const fruit = ['apple', 'banana', 'orange'];
    const result = fruit.join();
    console.log(result);
}

//Q2 make an array our of a string
{
    const fruit = 'apple, banana, cherry';
    const result = fruit.split(",");
    console.log(result);
}

//Q3 make this array look like this[5,4,3,2,1]
{
    const array = [1, 2, 3, 4, 5];
    const result = array.reverse();
    console.log(result);
}

//Q4 make new array without the first two elements
{
    const array = [1, 2, 3, 4, 5];
    const result = array.slice(2,5);
    console.log(array);
    console.log(result);
} 

class Student {
    constructor(name, age, enrolled, score){
        this.name = name;
        this.age = age;
        this.enrolled = enrolled;
        this.score = score;
    }
}

const students = [
    new Student ('A', 29, true, 45),
    new Student ('B', 28, false, 80),
    new Student ('C', 30, true, 90),
    new Student ('D', 40, false, 66),
    new Student ('E', 18, true, 88)
]
//Q5 find a student with the score 90
{
    for(let i = 0; i < students.length; i++){
        if(students[i].score >= 90){
            console.log(students[i].name);
        }
    }


    const result = students.find(function(student, index) {
        console.log(student, index);
    });
}

//Q6 make an array of enrolled students 
{
    const result = students.filter((student)=>student.enrolled);
    console.log(result);
}

