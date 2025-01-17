#!/bin/bash

# a. Crie uma pasta com seu nome
mkdir -p "symon-barreto"

# b. Dentro da pasta com seu nome crie uma pasta com o nome “resultado”
mkdir -p "symon-barreto/resultado"

# c. Baixe o arquivo hospedado
wget -q -O "symon-barreto/zip.zip" "https://vanilton.net/v1/download/zip.zip"

# d. Descompacte-o na raiz da pasta com seu nome
unzip -q "symon-barreto/zip.zip" -d "symon-barreto"

# e. Mova somente os arquivos descompactados (excluindo pastas específicas) para a pasta “resultado”
find "symon-barreto" -mindepth 1 -maxdepth 1 ! -name "zip.zip" ! -name "resultado" -exec mv -t "symon-barreto/resultado" {} +

# f. Remova o arquivo baixado
rm -f "symon-barreto/zip.zip"

# Exibir mensagem de conclusão
echo "Processo concluído! Arquivos descompactados estão em symon-barreto/resultado"
