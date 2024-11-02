# Traceroute Visual

O **Traceroute Visual** é um software inovador que utiliza a API do GeoIP2 e do Google Maps para executar traceroutes e mostrar graficamente as cidades por onde uma conexão de rede passa. É uma ferramenta poderosa para entender melhor o caminho que os dados percorrem na internet, tornando-se especialmente útil para profissionais de TI, estudantes e entusiastas.

## Funcionalidades

- Realiza traceroutes e visualiza os caminhos em um mapa interativo.
- Mostra as cidades intermediárias que a conexão passa.
- Interface intuitiva para fácil utilização.
- Acompanhamento em tempo real dos hops da conexão.

## Tecnologias Utilizadas

### Back-end
O back-end do software foi desenvolvido em Python utilizando o framework **Flask**, que fornece uma estrutura leve e eficiente para a construção de aplicações web. As principais bibliotecas utilizadas incluem:

- **aiohttp**: para realizar requisições assíncronas.
- **geoip2**: para obter informações geográficas a partir dos endereços IP.
- **scapy**: para manipulação de pacotes e execução do traceroute.

### Front-end
O front-end foi construído com JavaScript e utiliza a API do Google Maps para renderizar os mapas e as rotas de forma visual e interativa.

## Instalação

Para instalar e executar o projeto, siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/jbgoncalvess/traceroute-visual.git
