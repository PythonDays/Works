function when_level_clicked(event) {
  const images = document.querySelectorAll('img');
  let correctly_guessed = 0;

  images.forEach(img => {
    img.addEventListener('click', (event) => {
      if (track_number_of_correct_guess(event.target.getAttribute("src"))) {
        correctly_guessed++;
      }
    });
  });

  correctly_guessed += num_of_correct_pics();
  console.log(correctly_guessed + " hello");
}

function Create_board(event) {
  const clickedButton = parseInt(event.target.textContent);
  for (let i = 0; i < clickedButton * 5; i++) {
    let cards = document.createElement("img");
    cards.setAttribute("src", `./img/${Math.random() < 0.5 ? 1 : 2}.jpg`);
    cards.style.display = "inline";
    cards.style.padding = "5px";
    document.body.appendChild(cards);
  }

  setTimeout(() => {
    const images = document.querySelectorAll('img');
    let i = 0;
    images.forEach((img, index) => {
      i += 1;
      if (i !== 1) {
        img.setAttribute("id", index.toString());
        img.style.filter = "brightness(1%)";
      }
    });
    when_level_clicked(event);
  }, 3000);
}

function num_of_correct_pics() {
  const images = document.querySelectorAll('img');
  let correct = 0;
  images.forEach((img, index) => {
    if (img.getAttribute('src') === './img/1.jpg') {
      correct += 1;
    }
  });
  return correct;
}

function track_number_of_correct_guess(src) {
  if (src === './img/1.jpg') {
    console.log('Correct guess!');
    return true;
  } else {
    console.log('Incorrect guess.');
    return false;
  }
}

const buttons = document.querySelectorAll('button');
buttons.forEach(button => {
  button.addEventListener('click', (event) => Create_board(event));
});
