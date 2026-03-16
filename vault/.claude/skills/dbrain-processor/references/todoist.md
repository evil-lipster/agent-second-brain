# Google Tasks & Calendar Integration

## ВАЖНО: Два инструмента, разная логика

- **Google Tasks** — задачи без точного времени (to-do)
- **Google Calendar** — встречи, события с временем (онлайн/оффлайн общение)

Бот сам определяет куда класть по контексту записи.

---

## Task Links Format

Используй url из ответа MCP tool напрямую.

---

## Через mcp-cli

**ВСЕГДА используй mcp-cli. НЕ используй MCP tools напрямую.**

### Reading Tasks
```bash
# Список задач
mcp-cli call google-tasks list-tasks '{}'

# Задачи по списку
mcp-cli call google-tasks list-tasks '{"taskListId": "list_id"}'

# События календаря
mcp-cli call google-calendar list-events '{"timeMin": "today", "timeMax": "in 7 days"}'
```

### Writing Tasks
```bash
# Создать задачу
mcp-cli call google-tasks create-task '{"title": "Task", "due": "2026-03-20", "notes": "details"}'

# Завершить задачу
mcp-cli call google-tasks complete-task '{"taskId": "task_id"}'

# Обновить задачу
mcp-cli call google-tasks update-task '{"taskId": "task_id", "title": "New title"}'

# Создать событие в Calendar
mcp-cli call google-calendar create-event '{"summary": "Meeting", "start": "2026-03-20T10:00:00", "end": "2026-03-20T11:00:00"}'
```

---

## Pre-Creation Checklist

### 1. Check Workload (REQUIRED)
```bash
mcp-cli call google-tasks list-tasks '{}'
mcp-cli call google-calendar list-events '{"timeMin": "today", "timeMax": "in 7 days"}'
```

### 2. Check Duplicates (REQUIRED)

Если похожая задача уже есть → не создавать, отметить как дубликат.

---

## Priority by Domain

| Domain | Default Priority | Override |
|--------|-----------------|----------|
| Operational Excellence (urgent) | p1-p2 | — |
| Operational Excellence (regular) | p2-p3 | — |
| Agency Ops & Culture (urgent) | p2 | — |
| Agency Ops & Culture (regular) | p3 | — |
| Content (with deadline) | p2-p3 | — |
| Product/R&D | p4 | масштабируемость → p3 |
| AI & Tech | p4 | автоматизация → p3 |

### Priority Keywords

| Keywords in text | Priority |
|-----------------|----------|
| срочно, критично, горит | p1 |
| важно, приоритет, до конца недели | p2 |
| нужно, надо, не забыть | p3 |
| стратегия, R&D, долгосрочно | p4 |

### Priority Boost

Если запись совпадает с 2+ фильтрами → повысить приоритет на 1:
- Масштабируется на агентство?
- Можно автоматизировать?
- Усиливает операционную эффективность?
- Приближает к продукту или equity?

---

## Date Mapping

| Context | due |
|---------|-----|
| Срочные ops | today / tomorrow |
| На этой неделе | friday |
| На следующей неделе | next monday |
| Стратегия/R&D | in 7 days |
| Не указано | in 3 days |

### Russian → due

| Russian | due |
|---------|-----|
| сегодня | today |
| завтра | tomorrow |
| послезавтра | in 2 days |
| в понедельник | monday |
| в пятницу | friday |
| на этой неделе | friday |
| на следующей неделе | next monday |
| через неделю | in 7 days |
| 20 марта | 2026-03-20 |

---

## Task vs Event Detection
```
Entry contains...
│
├─ Время + онлайн/оффлайн общение? ──────> GOOGLE CALENDAR EVENT
│  (созвон, встреча, звонок, кофе, митинг)
│
└─ Всё остальное ────────────────────────> GOOGLE TASK
   (сделать, написать, подготовить, проверить)
```

---

## Task Creation
```bash
mcp-cli call google-tasks create-task '{"title": "Task title", "due": "2026-03-20", "notes": "context"}'
```

### Task Title Style

✅ Good:
- "Написать регламент онбординга"
- "Подготовить расчёт KPI по продуктам"
- "Запустить пилот автоматизации отчётности"

❌ Bad:
- "Подумать о регламенте"
- "Что-то с KPI"
- "Разобраться с автоматизацией"

### Workload Balancing

Если на день уже 3+ задачи → сдвинуть на следующий свободный день, упомянуть в отчёте.

---

## Task Lists Detection

| Keywords | Task List |
|----------|-----------|
| процесс, регламент, KPI, автоматизация | Operational Excellence |
| продукт, SaaS, MVP, монетизация | Product |
| команда, культура, найм, Wunder Digital | Agency Ops |
| пост, LinkedIn, контент, выступление | Content |

Если неясно → Inbox (без taskListId).

---

## Recurring Tasks
```bash
mcp-cli call google-tasks create-task '{"title": "Daily deep work: продуктовый портфель", "due": "every day at 9am", "notes": "process-goal"}'
```

### Recurring Patterns

| Описание | due pattern |
|----------|-------------|
| каждое утро | every day at 9am |
| каждый рабочий день | every weekday |
| раз в неделю | every monday |
| каждую пятницу | every friday |

---

## Anti-Patterns (НЕ СОЗДАВАТЬ)

- ❌ "Подумать о..." → конкретизируй действие
- ❌ "Разобраться с..." → что именно сделать?
- ❌ Абстрактные задачи без Next Action
- ❌ Дубликаты
- ❌ Задачи без дат

---

## Error Handling

CRITICAL: Никогда не предлагай "добавить вручную".

WRONG: "Не удалось добавить. Добавь вручную: Task title"
CORRECT: "Ошибка создания задачи: [exact error from MCP tool]"