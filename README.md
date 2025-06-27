# MLOps Course by Yandex Practicum

![MIT License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![GitHub repo size](https://img.shields.io/github/repo-size/Yandex-Practicum/mlops-course)
![GitHub last commit](https://img.shields.io/github/last-commit/Yandex-Practicum/mlops-course)

**Осваивайте на практике инструменты и подходы MLOps для построения воспроизводимых и стабильных ML-систем.**

## О курсе

Этот репозиторий содержит практические задания к курсу по MLOps. Каждое задание помогает освоить ключевые инструменты и подходы — от управления зависимостями до мониторинга ML-сервисов в продакшене.

## Структура репозитория

Каждый урок — это отдельная папка:
```
├── lesson-01-uv-env/
├── lesson-02-dependency-upgrade/
├── ...
└── README.md
```

# Быстрый старт

```bash
# Клонируйте только нужную папку (с помощью sparse-checkout)
git clone --filter=blob:none --sparse https://github.com/Yandex-Practicum/mlops-course.git
cd mlops-course
git sparse-checkout set lesson-01-uv-env
```
Альтернатива: просто клонировать весь репозиторий, если это не критично по объему:
```bash
git clone https://github.com/Yandex-Practicum/mlops-course.git
cd mlops-course/lesson-01-uv-env
```
# Вклад и обратная связь

Вы можете создавать Issues или Pull Requests, если находите ошибки или хотите улучшить задания. Мы ценим вклад сообщества 🙌

---

## Вклад и обратная связь

Вы можете создавать [Issues](https://github.com/Yandex-Practicum/mlops-course/issues) или присылать [Pull Requests](https://github.com/Yandex-Practicum/mlops-course/pulls), если находите ошибки или хотите улучшить задания. Мы ценим вклад сообщества.

---

## Лицензия

Проект распространяется под лицензией [MIT License](LICENSE).

---

## Авторы

Разработано командой [Яндекс Практикум](https://practicum.yandex.ru) при участии специалистов из индустрии.

<p align="left">
  <a href="https://practicum.yandex.ru/" target="_blank">
    <img src="https://avatars.githubusercontent.com/u/103542141?s=200&v=4" alt="Yandex Practicum Logo" width="120"/>
  </a>
</p>
