import java.util.Queue
import java.util.LinkedList

fun main() {
    val (n, k) = readln().split(" ").map { it.toInt() }
    val grid = List(n) { readln().trim().split(" ").map { it.toInt() } }
    val startPoints = List(k) {
        val (r, c) = readln().trim().split(" ").map { it.toInt() }
        Pair(r - 1, c - 1)
    }

    val queue: Queue<Pair<Int, Int>> = LinkedList()
    val visited = Array(n) { BooleanArray(n) { false } }
    
    for (point in startPoints) {
        val (y, x) = point
        visited[y][x] = true
        queue.add(x to y)
    }

    val dirs = listOf(0 to -1, 0 to 1, -1 to 0, 1 to 0)

    fun isInRange(x: Int, y: Int): Boolean {
        return x in 0 until n && y in 0 until n
    }

    while (queue.isNotEmpty()) {
        val (x, y) = queue.poll()

        for ((dx, dy) in dirs) {
            val (nx, ny) = x + dx to y + dy
            if (isInRange(nx, ny) && !visited[ny][nx] && grid[ny][nx] == 0) {
                visited[ny][nx] = true
                queue.add(nx to ny)
            }
        }
    }

    val answer = visited.sumOf { row -> row.count { it } }
    println(answer)
}