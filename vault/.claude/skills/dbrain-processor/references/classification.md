# Entry Classification

## Work Domains → Categories

### Operational Excellence
Автоматизация процессов, стандарты, инструкции, регламенты, KPI, расчёты, операционная эффективность

**Keywords:** процесс, автоматизация, регламент, стандарт, инструкция, KPI, расчёт, эффективность, оптимизация, метрика

**→ Category:** task (p1-p2) или project → Google Tasks

### AI & Tech
Инструменты, модели, промпты, пайплайны, агенты

**Keywords:** GPT, Claude, модель, агент, API, пайплайн, автоматизация, интеграция

**→ Category:** learning или project → thoughts/

### Product
Идеи, гипотезы, MVP, юнит-экономика, монетизация

**Keywords:** продукт, SaaS, MVP, гипотеза, монетизация, юнит-экономика, портфель

**→ Category:** idea или project → thoughts/

### Agency Ops & Culture
Команда, процессы, найм, управление, финансы, корпоративная культура, ценности, среда

**Keywords:** команда, найм, HR, финансы, Wunder Digital, агентство, культура, ценности, атмосфера, онбординг, Алеся, Даша, Мария, Олжас, Степан, Лизавета, Олеся, Дима, Макс

**→ Category:** task или project (depends on urgency)

### Content
Посты, идеи, тезисы для Telegram и LinkedIn, выступления

**Keywords:** пост, LinkedIn, контент, тезис, статья, выступление, Web Summit

**→ Category:** idea → thoughts/ideas/ или task если с дедлайном

### Cultural Insights
Антропологические наблюдения, культурные паттерны, искусство, история, связи между эпохами

**Keywords:** культура, антропология, паттерн, история, искусство, опера, балет, наблюдение, инсайт, цивилизация

**→ Category:** reflection → thoughts/reflections/

---

## Decision Tree
```
Entry text contains...
│
├─ Operational/urgent? ──────────────────────────> TASK (p1-p2)
│  (нужно сделать, дедлайн, не забыть, регламент готов)
│
├─ Process/standard to build? ───────────────────> PROJECT
│  (автоматизировать, стандартизировать, выстроить)
│
├─ AI/tech learning? ────────────────────────────> LEARNING
│  (узнал, модель, агент, интеграция, попробовала)
│
├─ Product/SaaS idea? ───────────────────────────> IDEA или PROJECT
│  (продукт, MVP, гипотеза, SaaS, портфель, монетизация)
│
├─ Strategic thinking? ──────────────────────────> PROJECT
│  (стратегия, план, R&D, долгосрочно, equity)
│
├─ Culture/team observation? ────────────────────> TASK или REFLECTION
│  (команда, культура, атмосфера, паттерн поведения)
│
├─ Cultural/anthropological insight? ────────────> REFLECTION
│  (наблюдение, связь эпох, искусство, антропология)
│
├─ Personal insight? ────────────────────────────> REFLECTION
│  (понял, осознал, философия)
│
└─ Content idea? ────────────────────────────────> IDEA
   (пост, тезис, контент, выступление)
```

---

## Status Keywords (для заметок и отчётов)

| Keywords | Интерпретация |
|----------|---------------|
| "внедрили", "запустили", "заработало" | Готово |
| "в процессе", "тестируем", "пилот" | В работе |
| "идея", "гипотеза", "надо проверить" | Бэклог |
| "застряло", "не работает", "блокер" | Требует внимания |
| "отменили", "не пошло", "закрыли" | Закрыто |

---

## Apply Decision Filters

Перед сохранением спроси:
- Это масштабируется на агентство?
- Это можно автоматизировать?
- Это усиливает операционную эффективность?
- Это приближает к продукту или equity?

Если да на 2+ вопроса → повысить приоритет.

---

## Photo Entries

1. Analyze image content via vision
2. Determine domain:
   - Схема процесса / регламент → Operational Excellence
   - Схема/диаграмма продукта → Product
   - Арт, культура, впечатление → Cultural Insights
   - Текст/статья → Learning
3. Add description to daily file

---

## Output Locations

| Category | Destination | Priority |
|----------|-------------|----------|
| task (ops) | Google Tasks | p1-p2 |
| task (culture/team) | Google Tasks | p2-p3 |
| task (content) | Google Tasks | p3-p4 |
| meeting/event | Google Calendar | — |
| idea | thoughts/ideas/ | — |
| reflection | thoughts/reflections/ | — |
| project | thoughts/projects/ | — |
| learning | thoughts/learnings/ | — |

---

## File Naming
```
thoughts/{category}/{YYYY-MM-DD}-short-title.md
```

---

## Thought Structure
```markdown
---
date: {YYYY-MM-DD}
type: {category}
domain: {Operational Excellence|AI & Tech|Product|Agency Ops & Culture|Content|Cultural Insights}
tags: [tag1, tag2]
---

## Context
[Что привело к мысли]

## Insight
[Ключевая идея]

## Implication
[Что это значит для Wunder Digital / продукта / стратегии]

## Next Action
[Конкретный шаг — не абстрактный]
```

---

## Anti-Patterns (ИЗБЕГАТЬ)

- Абстрактные рассуждения без Next Action
- Теория без применения к Wunder Digital
- Повторы без синтеза
- Задачи типа "подумать о..." (конкретизируй!)

---

## MOC Updates

After creating thought file, add link to:
```
MOC/MOC-{category}s.md
```