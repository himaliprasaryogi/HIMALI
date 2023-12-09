'use strict';

        const year = parseInt(prompt("Enter a year:"));

        let isLeapYear = false;

        if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
            isLeapYear = true;
        }

       console.log("Leap Year Checker");
        console.log(" year" + " is " + (isLeapYear ? "a leap year." : "not a leap year."));