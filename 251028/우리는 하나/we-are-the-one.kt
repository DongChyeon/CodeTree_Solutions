import java.util.Queue
import java.util.LinkedList
import kotlin.math.abs
import kotlin.math.max

fun <T> List<T>.combinations(r: Int): List<List<T>> {
    val result = mutableListOf<T>()
    val combinations = mutableListOf<List<T>>()

    fun dfs(start: Int) {
        if (result.size == r) {
            combinations.add(result.toList())
            return
        }

        for (i in start until this.size) {
            result.add(this[i])
            dfs(i + 1)
            result.removeLast()
        }
    }

    dfs(0)
    return combinations
}

fun main() {
    val (n, k, u, d) = readln().trim().split(" ").map { it.toInt() }
    val grid = Array(n) { readln().trim().split(" ").map { it.toInt() } }

    val cities = mutableListOf<Pair<Int, Int>>()
    for (y in 0 until n) {
        for (x in 0 until n) {
            cities.add(Pair(x, y))
        }
    }

    var answer = 0
    val dirs = listOf(0 to -1, 0 to 1, -1 to 0, 1 to 0)

    fun isInRange(x: Int, y: Int) : Boolean {
        return x in 0 until n && y in 0 until n
    }

    fun canGo(x: Int, y: Int, nx: Int, ny: Int, visited: Array<BooleanArray>) : Boolean {
        return isInRange(nx, ny) && !visited[ny][nx] && abs(grid[ny][nx] - grid[y][x]) in u until d + 1
    }

    for (comb in cities.combinations(k)) {
        val queue: Queue<Pair<Int, Int>> = LinkedList()
        val visited = Array(n) { BooleanArray(n) { false } }

        for ((x, y) in comb) {
            visited[y][x] = true
            queue.add(x to y)
        }

        while (queue.isNotEmpty()) {
            val (x, y) = queue.poll()
            for ((dx, dy) in dirs) {
                val (nx, ny) = Pair(x + dx, y + dy)
                if (canGo(x, y, nx, ny, visited)) {
                    visited[ny][nx] = true
                    queue.add(nx to ny)
                }
            }
        }

        val result = visited.sumOf { row -> row.count { it } }
        answer = max(answer, result)
    }

    println(answer)
}