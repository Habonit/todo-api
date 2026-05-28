import { TodoItem } from './TodoItem'
import styles from './TodoList.module.css'

export function TodoList({ todos, onComplete, onDelete }) {
  if (todos.length === 0) {
    return (
      <div className={styles.empty}>
        <p>No todos yet. Add one above!</p>
      </div>
    )
  }

  return (
    <ul className={styles.list}>
      {todos.map((todo) => (
        <TodoItem
          key={todo.id}
          todo={todo}
          onComplete={onComplete}
          onDelete={onDelete}
        />
      ))}
    </ul>
  )
}
