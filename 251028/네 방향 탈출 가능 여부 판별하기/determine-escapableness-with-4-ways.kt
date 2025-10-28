import java.util.Queue
import java.util.LinkedList

fun main() {
    val (n, m) = readln().trim().split(" ").map { it.toInt() }
    val grid = List(n) { readln().trim().split(" ").map { it.toInt() } }

    val visited = Array(n) { BooleanArray(m) { false } }
    val queue: Queue<Pair<Int, Int>> = LinkedList()
    val dirs = listOf(0 to -1, 0 to 1, -1 to 0, 1 to 0)

    queue.add(0 to 0)
    visited[0][0] = true

    fun isInRange(x: Int, y: Int): Boolean {
        return 0 <= x && x < m && 0 <= y && y < n
    }

    while (queue.isNotEmpty()) {
        val (x, y) = queue.poll()
        if (x == m - 1 && y == n - 1) {
            println("1")
            return
        }

        for ((dx, dy) in dirs) {
            val (nx, ny) = x + dx to y + dy

            if (isInRange(nx, ny) && !visited[ny][nx] && grid[ny][nx] == 1) {
                visited[ny][nx] = true
                queue.add(nx to ny)
            }
        } 
    }

    println("0")
}