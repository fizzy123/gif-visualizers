var gifcount, position, numbers;

gifcount = 155;
position = 0;
numbers = [];
for (i = 0; i < gifcount; i++) {
	numbers.push(i+1);
}
numbers = shuffle(numbers);

function change() {
	document.getElementById("assholedumbass").src = "gif (" + numbers[position] + ").gif";
    position++;
    if (position === gifcount) {
    	position = 0;
    	numbers = shuffle(numbers);
    }

    setTimeout(change, 30000);
}

function shuffle(array) {
    var counter = array.length, temp, index;

    // While there are elements in the array
    while (counter > 0) {
        // Pick a random index
        index = Math.floor(Math.random() * counter);

        // Decrease counter by 1
        counter--;

        // And swap the last element with it
        temp = array[counter];
        array[counter] = array[index];
        array[index] = temp;
    }

    return array;
}

setTimeout(change, 10);