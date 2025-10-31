import kotlin.math.min

fun main() {
    val n = readln().trim().toInt()
    val matrix = Array(n) { readln().trim().split(" ").map { it.toInt() } }
    val dp = List(n) { IntArray(n) { 0 } }

    dp[0][n - 1] = matrix[0][n - 1]
    for (y in 1 until n) {
        dp[y][n - 1] = dp[y - 1][n - 1] + matrix[y][n - 1]
    }
    for (x in n - 2 downTo 0) {
        dp[0][x] = dp[0][x + 1] + matrix[0][x]
    }

    for (y in 1 until n) {
        for (x in n - 2 downTo 0) {
            dp[y][x] = min(dp[y - 1][x], dp[y][x + 1]) + matrix[y][x]
        }
    }

    //for (row in dp) println(row.joinToString(" "))

    println(dp[n - 1][0])
}