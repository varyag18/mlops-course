# MLOps Course by Yandex Practicum

![MIT License](https://img.shields.io/badge/license-MIT-green)
![GitHub repo size](https://img.shields.io/github/repo-size/Yandex-Practicum/mlops-course)

## Осваивайте на практике инструменты и подходы MLOps для построения воспроизводимых и стабильных ML-систем.

### О курсе

Этот репозиторий содержит практические задания к курсу по MLOps. Каждое задание помогает освоить ключевые инструменты и подходы — от управления зависимостями до мониторинга ML-сервисов в продакшне.

### Структура репозитория

Каждый урок — это отдельная папка:
```
├── lesson-01-uv-env/
├── lesson-02-dependency-upgrade/
├── ...
├── LICENSE
└── README.md
```

### Быстрый старт

Клонируйте только нужную папку с уроком с помощью sparse-checkout, не загружая весь репозиторий:

```bash
git clone --filter=blob:none --sparse https://github.com/Yandex-Practicum/mlops-course.git
cd mlops-course
git sparse-checkout set <lesson-folder-name>  # например: lesson-01-uv-env
```
Если объём не критичен, можно просто клонировать весь репозиторий:

```bash
git clone https://github.com/Yandex-Practicum/mlops-course.git
cd mlops-course/lesson-01-uv-env # или другой нужный урок
```

### Вклад и обратная связь

Вы можете создавать [Issues](https://github.com/Yandex-Practicum/mlops-course/issues) или присылать [Pull Requests](https://github.com/Yandex-Practicum/mlops-course/pulls), если находите ошибки или хотите улучшить задания. Мы ценим вашу обратную связь!


### Лицензия

Проект распространяется под лицензией [MIT License](LICENSE).


### Авторы

Разработано командой [Яндекс Практикум](https://practicum.yandex.ru) при участии специалистов из индустрии.
