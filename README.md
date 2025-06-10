# Django Learning Repository

<img src="https://i.imgur.com/ahjHe3h.jpeg" width="500" height="200">

---

***
Esse projeto é utilizado para aprender a usar o web FrameWork Django

___


Inicialmente optamos por padronizar as ***settings*** do VSCode. As configurações escolhidas foram as seguintes:

```json
{
    "window.zoomLevel": 0,
    "python.languageServer": "Pylance", // ms-python.vscode-pylance
    "python.testing.unittestEnabled": false, // ms-python.python
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": [], // -x to bail
    "python.linting.flake8Enabled": true,
    "python.linting.mypyEnabled": true,
    "python.linting.pylintArgs": [
      "--load-plugins=pylint_django",
      "--errors-only"
    ],
    "python.formatting.autopep8Args": ["--indent-size=4"],
//    "python.defaultInterpreterPath": "venv/bin/python",
    "[python]": {
      "editor.defaultFormatter": "ms-python.python", // ms-python.python
      "editor.tabSize": 4,
      "editor.insertSpaces": true,
      "editor.formatOnSave": true,
      "editor.formatOnType": true,
      "editor.codeActionsOnSave": {
        "source.organizeImports": "explicit"
      }
    },
    "[html]": {
      "editor.formatOnSave": true,
      "editor.defaultFormatter": "vscode.html-language-features",
      "editor.quickSuggestions": {
        "other": true,
        "comments": true,
        "strings": true
      }
    },
    "[django-html]": {
      "editor.formatOnSave": false,
      "editor.defaultFormatter": "vscode.html-language-features",
      "editor.quickSuggestions": {
        "other": true,
        "comments": true,
        "strings": true
      }
    },
    "files.associations": {
      "*.js": "javascript",
      "*.jsx": "javascriptreact",
      "*.xml": "html",
      "*.svg": "html",
      "*.html": "html",
      "django-html": "html", // batisteo.vscode-django
      "**/*.html": "html",
      "**/templates/**/*.html": "django-html",
      "**/base_templates/**/*.html": "django-html",
      "**/requirements{/**,*}.{txt,in}": "pip-requirements"
    },
    "emmet.includeLanguages": {
      "django-html": "html", // batisteo.vscode-django
      "javascript": "javascriptreact",
      "typescript": "typescriptreact"
    },
    "workbench.colorTheme": "Dracula Soft"
  }
  ```

As configurações foram retiradas do curso de Django que fiz do Otávio Miranda.



## Uso do commitizen

Nesse projeto foi optado por testar o uso de uma ferramenta auxiliar para commits, o ***Commitizen*** (https://commitizen-tools.github.io/commitizen/). Segue o passo a passo da configuração dele no projeto e algumas explicações:

- Primeiro passo: Conferir se o ***nodejs*** está instalado globalmente na máquina. Para isso, deve-se utilizar o seguinte comando: ```node -v```. Se a versão aparecer, então significa que está instalado, se não, deve ir até o site https://nodejs.org/pt e baixar via ***LTS***;

- Segundo passo: Depois de instalar e configurar o ***nodejs*** verifique se o ***npm*** está sendo reconhecido através do seguinte comando: ```npm -v```. Se a versão aparecer, então significa que está instalado, se não, deve reiniciar o terminal e verificar novamente o ***nodejs***. Se o erro persistir, busque informações em forum ou IA's;

Nesse projeto temos o desenvolvimento do que foi aprendido nesse curso, tudo foi feito em uma única branch (***main***);