// Exibir o botão "Voltar ao Topo" ao rolar a página
window.addEventListener("scroll", function () {
    document.querySelector('.back-to-top').style.display = window.scrollY > 200 ? 'block' : 'none';
});