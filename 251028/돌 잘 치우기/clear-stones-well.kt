import java.util.Queue
import java.util.LinkedList
import kotlin.math.max

fun <T> List<T>.combinations(r: Int): List<List<T>> {
    val result = mutableListOf<List<T>>()
    fun dfs(start: Int, comb: MutableList<T>) {
        if (comb.size == r) {
            result.add(comb.toList())
            return
        }
        for (i in start until this.size) {
            comb.add(this[i])
            dfs(i + 1, comb)
            comb.removeLast()
        }
    }
    dfs(0, mutableListOf())
    return result
}

fun main() {
    val (n, k, m) = readln().trim().split(" ").map { it.toInt() }
    val grid = Array(n) { readln().trim().split(" ").map { it.toInt() } }
    val stonePos = mutableListOf<Pair<Int, Int>>()
    for (i in 0 until n) {
        for (j in 0 until n) {
            if (grid[i][j] == 1) {
                stonePos.add(i to j)
            }
        }
    }
    val startPos = mutableListOf<Pair<Int, Int>>()
    repeat(k) {
        val (r, c) = readln().trim().split(" ").map { it.toInt() }
        startPos.add(r - 1 to c - 1)
    }

    fun isInRange(x: Int, y: Int) : Boolean { 
        return x in 0 until n && y in 0 until n
    }

    var answer = 0

    for (comb in stonePos.combinations(stonePos.size - m)) {
        val visited = Array(n) { BooleanArray(n) { false } }
        val queue: Queue<Pair<Int, Int>> = LinkedList()

        val dirs = listOf(0 to -1, 0 to 1, -1 to 0, 1 to 0)

        for ((startX, startY) in startPos) {
            queue.add(startX to startY)
            visited[startY][startX] = true
        }

        while (queue.isNotEmpty()) {
            val (x, y) = queue.poll()
            for ((dx, dy) in dirs) {
                val (nx, ny) = x + dx to y + dy
                if (isInRange(nx, ny) && !visited[ny][nx] && Pair(nx, ny) !in comb) {
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