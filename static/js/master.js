window.addEventListener('click', filter, false);
var spin = document.getElementsByClassName("spin"); // or:
function filter(e){
  if (e.target.tagName === 'A'){ // провека что кликнули на ссылку
    console.log(e.target.href);  // получаем URL адрес ссылки
    e.preventDefault();          // отменяем переход
    spin[0].style.display = "flex";
    window.location.href = e.target.href; // переходите по ссылке
  }
}
