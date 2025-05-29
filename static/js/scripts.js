// Função genérica para enviar formulários via AJAX e exibir resultados
async function handleForm(formId, endpoint) {
  const form = document.getElementById(formId);
  const resultEl = document.getElementById('result');

  form.addEventListener('submit', async e => {
    e.preventDefault();

    // Desabilita o botão enquanto aguarda
    const btn = form.querySelector('button');
    btn.disabled = true;
    btn.textContent = 'Processando...';

    const data = new FormData(form);
    const resp = await fetch(endpoint, {
      method: 'POST',
      body: data
    });

    const json = await resp.json();
    if (resp.ok) {
      resultEl.textContent = 
        `Raiz: ${json.root}\nIterações: ${json.iterations}\nErro: ${json.error}`;
    } else {
      resultEl.textContent = `Erro: ${json.error}`;
    }

    // Restaura o botão
    btn.disabled = false;
    btn.textContent = 'Calcular';
  });
}

// Inicializa ambos os formulários quando a página carrega
window.addEventListener('DOMContentLoaded', () => {
  handleForm('false-pos-form',   '/false-position/');
  handleForm('secant-form',      '/secant/');
});
