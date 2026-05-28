import { useState, useEffect, useCallback } from 'react'
import { fetchTodos, createTodo, completeTodo, deleteTodo } from './api'
import { AddTodo } from './components/AddTodo'
import { TodoList } from './components/TodoList'
import styles from './App.module.css'

export default function App() {
  const [todos, setTodos] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  const loadTodos = useCallback(async () => {
    try {
      const data = await fetchTodos()
      setTodos(data)
    } catch {
      setError('Could not load todos. Is the backend running?')
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => {
    loadTodos()
  }, [loadTodos])

  async function handleAdd(title) {
    try {
      const todo = await createTodo(title)
      setTodos((prev) => [...prev, todo])
    } catch {
      setError('Failed to add todo.')
    }
  }

  async function handleComplete(id) {
    try {
      const updated = await completeTodo(id)
      setTodos((prev) => prev.map((t) => (t.id === id ? updated : t)))
    } catch {
      setError('Failed to complete todo.')
    }
  }

  async function handleDelete(id) {
    try {
      await deleteTodo(id)
      setTodos((prev) => prev.filter((t) => t.id !== id))
    } catch {
      setError('Failed to delete todo.')
    }
  }

  const pending = todos.filter((t) => !t.completed).length
  const total = todos.length

  return (
    <div className={styles.page}>
      <header className={styles.header}>
        <h1 className={styles.title}>Todo</h1>
        {total > 0 && (
          <p className={styles.subtitle}>
            {pending} of {total} remaining
          </p>
        )}
      </header>

      <main className={styles.card}>
        <div className={styles.inputArea}>
          <AddTodo onAdd={handleAdd} />
        </div>

        {error && (
          <div className={styles.errorBanner}>
            {error}
            <button className={styles.dismissBtn} onClick={() => setError(null)}>✕</button>
          </div>
        )}

        {loading ? (
          <div className={styles.loading}>Loading…</div>
        ) : (
          <TodoList
            todos={todos}
            onComplete={handleComplete}
            onDelete={handleDelete}
          />
        )}
      </main>
    </div>
  )
}
