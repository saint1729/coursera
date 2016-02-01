var target;
var guess_input_string;
var guess_input;
var finished = false;
var guesses = 0;
var colors = ["blue", "green", "indigo", "red", "orange", "violet", "yellow"];

function colorGuessingGame() {
    var random_number = Math.random()*colors.length;
    var random_number_integer = Math.floor(random_number);
    target = colors[random_number_integer];

    while(!finished) {
        guess_input_string = prompt("I am thinking of a color from the following:\n\n"+
                                    colors+
                                    "What is the color?");
        //guess_input = colors.indexOf(guess_input_string);
        guesses += 1;
        finished = check_guess();
    }
}

function check_guess() {
    if(colors.indexOf(guess_input_string) < 0) {
        alert("Sorry, I don't recognize your color.\n\nPlease try again.");
        return false;
    }
    if(guess_input_string > target) {
        alert("Sorry, Your guess is not correct.\n\nHint: Your color is higher.\n\nPlease try again.");
        return false;
    }
    if(guess_input_string < target) {
        alert("Sorry, Your guess is not correct.\n\nHint: Your color is lower.\n\nPlease try again.");
        return false;
    }
    alert("Congratulations! " + target + " is the color. You took " + guesses + " guesses.\n\n");
    myBody = document.getElementsByTagName("body")[0];
    myBody.style.background = target;
    return true;
}
