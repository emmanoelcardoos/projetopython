from setuptools import setup, find_packages

setup(
    name="projetopyhon",  # Nome do pacote
    version="0.1.0",  # Versão do pacote
    author="",
    author_email="seu.email@exemplo.com",
    description="Análise de Sentimentos com base em dados de tweets relacionados a companhias aéreas.",
    long_description=open("README.md").read(),  # Lendo o conteúdo do README.md
    long_description_content_type="text/markdown",
    url="https://github.com/seu_usuario/analise_sentimentos",  # Link do repositório
    packages=find_packages(),  # Procura automaticamente pelos pacotes no diretório
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',  # Versões do Python suportadas
    install_requires=[  # Dependências do pacote
        "pandas>=1.3.0",
    ],
    entry_points={  # Se tiver um ponto de entrada para scripts, configure aqui
        "console_scripts": [
            "analise_sentimentos=main:main",
        ]
    },
)
