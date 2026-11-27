//Catálogo de jogos
const tabela = document.getElementById("tabela-jogos");
const mensagem = document.getElementById("mensagem");

// Formato de moeda brasuleira para o preço
const moeda = {style: "currency", currency:"BRL"};

//Mostra um aviso na página - tipo: "info", "sucesso" ou "erro"
function mostraMensagem(texto, tipo) {
    mensagem.textContent = texto;
    mensagem.className = "mensagem" + tipo;
}

// Busca uma rota da API e devolver o JSON já convertido
// em objeto javascript
async function buscar(rota) {
    const resposta = await fetch(`${API_URL} ${rota}`);
    //404,500... Vira um erro que será tratado por quem mandou
    if(!resposta.ok) {
        throw new Error(`Erro ${resposta.status} em ${rota}`);
    }
    return await resposta.json();
}
// Criar uma célula <td> com texto informado
function criarCelula(texto, classe) {
    const td = document.createElement("td");
    td.textContent = texto;
    if (classe) {
        td.className = classe;
  }
  return td;
}

async function carregarJogos() {
    mostraMensagem("Carregando jogos...", "info");
    tabela.innerHTML = "";

    try {
        const plataforma = await buscar("/plataformas/");
        const jogos = await buscar("/jogos/");

        // Dicionário id -> nome (ex: {1: "playStation 5"})
        const nomes = {};
        plataforma.forEach(function (plataforma){
            nomes[plataforma.id] = plataforma.name;
        });
        if (jogos.lenght === 0) {
            mostraMensagem("Nenhum jogo cadastrado ainda", "info");
            return;
        }
        jogos.for.Each(function (jogo){
            const linha = document.createElement("tr");

            linha.appendChild(criarCelula(jogo.id));
            linha.appendChild(criarCelula(jogo.titulo));
            linha.appendChild(criarCelula(jogo.genero));

            const preco = jogo.preco.tolocaleString("pt-BR", moeda);
            linha.appendChild(criarCelula(preco, "direita"));

            linha.appendChild(criarCelula(nome[jogo.plataforma] || "-"));
            linha.appendChild(criarCelula("", "acoes"));

            tabela.appendChild(linha);
        });
        mostraMensagem("", "info");
    }catch (erro) {
        mostraMensagem(
            "Não foi possivel carregar os jogos. API está rodando?",
            "erro"
        );
        console.erro(erro);
    }
}
carregarJogos();