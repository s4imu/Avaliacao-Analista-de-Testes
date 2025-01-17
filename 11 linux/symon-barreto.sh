# a. Crie uma pasta com seu nome
echo "Criando pasta: symon-barreto..."
mkdir -p "symon-barreto"

# b. Dentro da pasta com seu nome crie uma pasta com o nome "resultado"
echo "Criando pasta: resultado dentro da pasta: symon-barreto..."
mkdir -p symon-barreto/resultado

# c. Baixe o arquivo hospedado: https://vanilton.net/v1/download/zip.zip
echo "Baixando o arquivo zip..."
wget -O symon-barreto/zip.zip  https://vanilton.net/v1/download/zip.zip

# d. Descompacte-o na raiz da pasta com seu nome
echo "Descompactando arquivo na raiz da pasta symon-barreto..."
unzip symon-barreto/zip.zip -d symon-barreto

# e. Mova somente os arquivos descompactados (excluindo pastas específicas) para a pasta "resultado"
echo "Movendo arquivos descompactados para a pasta resultado..."
mv symon-barreto/readme.md symon-barreto/resultado/

# f. Remova o arquivo baixado
echo "Excluindo arquivo baixado..."
rm -f symon-barreto/zip.zip

echo "Concluído! Arquivos descompactados se encontram em symon-barreto/resultado"
