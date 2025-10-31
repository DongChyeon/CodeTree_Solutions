import kotlin.math.max
import kotlin.math.min

fun main() {
    val n = readln().trim().toInt()
    val grid = Array(n) { readln().trim().split(" ").map { it.toInt() }.toIntArray() }
    val dp = Array(n) { IntArray(n) { Int.MAX_VALUE } }

    fun initialize() {
        for (y in 0 until n) {
            for (x in 0 until n) {
                dp[y][x] = Int.MAX_VALUE
            }
        }

        dp[0][0] = grid[0][0]

        for (y in 1 until n) dp[y][0] = max(dp[y - 1][0], grid[y][0])
        for (x in 1 until n) dp[0][x] = max(dp[0][x - 1], grid[0][x])
    }

    fun solve(lowerBound: Int) : Int {
        for (y in 0 until n) {
            for (x in 0 until n) {
                if (grid[y][x] < lowerBound) grid[y][x] = Int.MAX_VALUE
            }
        }

        initialize()

        for (y in 1 until n) {
            for (x in 1 until n) {
                dp[y][x] = max(min(dp[y - 1][x], dp[y][x - 1]), grid[y][x])
            }
        }

        return dp[n - 1][n - 1];
    }

    var answer = 100
    val maxVal = grid.maxOf { row -> row.maxOrNull()!! }

    for (lowerBound in 1 until maxVal + 1) {
        val upperBound = solve(lowerBound)

        if (upperBound == Int.MAX_VALUE) continue

        answer = min(answer, upperBound - lowerBound)
    }

    println(answer)
}