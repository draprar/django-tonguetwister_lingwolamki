const mybutton = document.getElementById("topBtn");

window.onscroll = () => {
  if (window.pageYOffset > 1) {
    myButton.style.display = "block";
  } else {
    myButton.style.display = "none";
  }
};

const topFunction = () => {
  window.scrollTo({ top: 0, behavior: 'smooth'})
};