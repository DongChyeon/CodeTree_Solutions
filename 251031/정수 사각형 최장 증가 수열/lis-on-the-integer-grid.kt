import java.util.PriorityQueue
import kotlin.math.max

fun main() {
    val n = readln().trim().toInt()
    val grid = Array(n) { readln().trim().split(" ").map { it.toInt() }.toIntArray() }
    val dp = Array(n) { IntArray(n) { 1 } }
    val pq = PriorityQueue<Triple<Int, Int, Int>>(compareBy { it.first })

    var answer = 1

    fun inRange(x: Int, y: Int) : Boolean {
        return x in 0 until n && y in 0 until n
    }

    for (y in 0 until n) {
        for (x in 0 until n) {
            pq.add(Triple(grid[y][x], x, y))
        }
    }

    val dirs = listOf(0 to -1, 0 to 1, -1 to 0, 1 to 0)

    while (pq.isNotEmpty()) {
        val (num, x, y) = pq.poll()
        for ((dx, dy) in dirs) {
            val (nx, ny) = x + dx to y + dy
            if (inRange(nx, ny) && grid[y][x] > grid[ny][nx]) {
                dp[y][x] = max(dp[y][x], dp[ny][nx] + 1)
                answer = max(answer, dp[y][x])
            }
        }
    }

    println(answer)
}