import kotlin.math.max
import kotlin.math.min

fun main() {
    val n = readLine()!!.trim().toInt()
    val grid = List(n) { readln().trim().split(" ").map { it.toInt() } }

    var answer = 0
    val visited = BooleanArray(n) { false }

    fun choose(depth: Int, minNum: Int) {
        if (depth == n) {
            answer = max(answer, minNum)
            return
        }

        for (num in 0 until n) {
            if (visited[num]) continue

            visited[num] = true
            choose(depth + 1, min(minNum, grid[depth][num]))
            visited[num] = false
        }
    }

    choose(0, Int.MAX_VALUE)

    println(answer)
}