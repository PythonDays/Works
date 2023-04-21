const buttons = document.querySelectorAll('button');

buttons.forEach(button => {
  button.addEventListener('click', handleClick);
});

function handleClick(event) {
  const clickedButton = event.target;
  if (clickedButton.textContent === "HTML"){
      const topicsDiv= document.querySelector('.topics')
      const topics=["Elements", "Attributes", "Links", "Images", "Lists", "Tables", "Forms", "Multimedia", "Semantics", "Accessibility"]
      topicsDiv.innerHTML = "";
      for (let i = 0; i <= 9; i++) {
          const newButton = document.createElement('button');
          newButton.textContent =topics[i]
          topicsDiv.appendChild(newButton)
          newButton.addEventListener('click', handleClick)
      }
}
    if (clickedButton.textContent === "CSS"){
      const topicsDiv= document.querySelector('.topics');
      const topics=["Selectors","Box Model","Typography","Flexbox","Grid","Colors","Transitions","Animations","Media Queries","Responsive Design"];
      topicsDiv.innerHTML = "";
      for (let i = 0; i <= 9; i++) {
          const newButton = document.createElement('button');
          newButton.textContent =topics[i]
          topicsDiv.appendChild(newButton)
          newButton.addEventListener('click', handleClick)
      }
  }
  if (clickedButton.textContent === "Javascript"){
      const topicsDiv= document.querySelector('.topics');
      const topics=["Variables","Functions","Events","Loops","Conditions","Arrays","Objects","DOM Manipulation","Promises","Async/Await"];
      topicsDiv.innerHTML = "";
      for (let i = 0; i <= 9; i++) {
          const newButton = document.createElement('button');
          newButton.textContent =topics[i]
          topicsDiv.appendChild(newButton)
          newButton.addEventListener('click', handleClick)
      }}
  if (clickedButton.textContent !== "Javascript" && clickedButton.textContent !== "CSS" && clickedButton.textContent !== "HTML"){
      let info = document.getElementById(clickedButton.textContent);
      let allParagraphs = document.getElementsByTagName("p");
      for (let i = 0; i < allParagraphs.length; i++) {
        allParagraphs[i].style.display = "none";
}
      info.style.display = "block";

  }
  }

