import styles from './TodoItem.module.css'

export function TodoItem({ todo, onComplete, onDelete }) {
  return (
    <li className={`${styles.item} ${todo.completed ? styles.completed : ''}`}>
      <button
        className={styles.checkBtn}
        onClick={() => !todo.completed && onComplete(todo.id)}
        aria-label={todo.completed ? 'Completed' : 'Mark as complete'}
        disabled={todo.completed}
      >
        {todo.completed ? (
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
            <polyline points="20 6 9 17 4 12" />
          </svg>
        ) : null}
      </button>

      <span className={styles.title}>{todo.title}</span>

      <button
        className={styles.deleteBtn}
        onClick={() => onDelete(todo.id)}
        aria-label="Delete todo"
      >
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
          <line x1="18" y1="6" x2="6" y2="18" />
          <line x1="6" y1="6" x2="18" y2="18" />
        </svg>
      </button>
    </li>
  )
}
