function when_level_clicked(){
  const images = document.querySelectorAll('img');
  const num_of_correct_images = num_of_correct_pics()
  const total_num_of_images = check_how_many_images()
  var correctly_guessed = 0
  images.forEach(img => {
    img.addEventListener('click', ()=>{
      if
      (track_number_of_correct_guess(event.target.getAttribute("src"))===true){
        correctly_guessed++
      }
  });
  correctly_guessed += track_number_of_correct_guess()
  console.log(correctly_guessed + "hello")
}

function Create_board(event){
  const clickedbutton= parseInt(event.target.textContent)
  for (let i = 0; i <= clickedbutton*5; i++) {
    let cards= document.createElement("img")
    cards.setAttribute("src", `./img/${Math.random()< 0.5 ? 1 : 2}.jpg`)
    cards.style.display = "in-line";
    cards.style.padding= "5px";
    document.body.appendChild(cards);
  }
