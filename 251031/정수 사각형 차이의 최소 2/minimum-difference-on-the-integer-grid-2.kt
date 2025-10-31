import kotlin.math.max
import kotlin.math.min

fun main() {
    val n = readln().trim().toInt()
    val grid = Array(n) { readln().trim().split(" ").map { it.toInt() } }
    val dp = Array(n) { Array(n) { Triple(100, 0, 100) } } // 최대-최소, 최대, 최소
    dp[0][0] = Triple(0, grid[0][0], grid[0][0])

    for (x in 1 until n) {
        val maxVal = max(dp[0][x - 1].second, grid[0][x])
        val minVal = min(dp[0][x - 1].third, grid[0][x])
        dp[0][x] = Triple(maxVal - minVal, maxVal, minVal)
    }
    for (y in 1 until n) {
        val maxVal = max(dp[y - 1][0].second, grid[y][0])
        val minVal = min(dp[y - 1][0].third, grid[y][0])
        dp[y][0] = Triple(maxVal - minVal, maxVal, minVal)
    }

    for (y in 1 until n) {
        for (x in 1 until n) {
            val candidates = mutableListOf<Triple<Int, Int, Int>>()
            val fromUp = max(dp[y - 1][x].second, grid[y][x]) - min(dp[y - 1][x].third, grid[y][x])
            val fromLeft = max(dp[y][x - 1].second, grid[y][x]) - min(dp[y][x - 1].third, grid[y][x])

            candidates.add(Triple(fromUp, max(dp[y - 1][x].second, grid[y][x]), min(dp[y - 1][x].third, grid[y][x])))
            candidates.add(Triple(fromLeft, max(dp[y][x - 1].second, grid[y][x]), min(dp[y][x - 1].third, grid[y][x])))
            
            dp[y][x] = candidates.sortedWith(
                compareBy<Triple<Int, Int, Int>> { it.first }
                    .thenBy { it.second }
                    .thenByDescending { it.third }
            ).first()
        }
    }

    println(dp[n - 1][n - 1].first)
}