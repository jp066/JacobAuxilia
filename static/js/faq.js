const questions = document.querySelectorAll('.faq-question');
// Adiciona um evento de clique para cada pergunta
questions.forEach(question => {
    question.addEventListener('click', () => {
        const answer = question.nextElementSibling;
        // Alterna entre mostrar e esconder a resposta com transição suave
        if (answer.style.display === 'block') {
            answer.style.display = 'none';
            answer.classList.remove('show');
        } else {
            answer.style.display = 'block';
            setTimeout(() => {
                answer.classList.add('show');
            }, 10);  // Tempo para garantir que o display seja alterado antes da animação
        }
    });
});