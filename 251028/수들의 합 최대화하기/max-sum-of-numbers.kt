import kotlin.math.max

fun main() {
    val n = readLine()!!.toInt()
    val grid = Array(n) { readLine()!!.split(" ").map { it.toInt() } }
    val visited = BooleanArray(n) { false }

    val choosedTiles: MutableList<Int> = mutableListOf()
    var answer = 0

    fun choose(depth: Int) {
        if (depth == n) {
            answer = max(choosedTiles.sum(), answer)
            return
        }

        for (num in 0 until n) {
            if (visited[num]) continue

            choosedTiles.add(grid[depth][num])
            visited[num] = true
            choose(depth + 1)
            choosedTiles.removeLast()
            visited[num] = false
        }
    }

    choose(0)

    println(answer)
}