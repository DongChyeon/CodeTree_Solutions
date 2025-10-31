import kotlin.math.max
import kotlin.math.min

fun main() {
    val n = readln().trim().toInt()
    val matrix = List(n) { readln().trim().split(" ").map { it.toInt() } }
    val dp = Array(n) { IntArray(n) { 1000000 } }

    dp[0][0] = 0
    for (x in 1 until n) dp[0][x] = max(dp[0][x - 1], matrix[0][x])
    for (y in 1 until n) dp[y][0] = max(dp[y - 1][0], matrix[y][0])

    for (y in 1 until n) {
        for (x in 1 until n) {
            dp[y][x] = max(min(dp[y - 1][x], dp[y][x - 1]), matrix[y][x])
        }
    }

    println(dp[n - 1][n - 1])
}