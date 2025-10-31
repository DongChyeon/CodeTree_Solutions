import kotlin.math.max

fun main() {
    val n = readLine()!!.trim().toInt()
    val matrix = List(n) { readLine()!!.trim().split(" ").map { it.toInt() } }
    val dp = List(n) { IntArray(n) { 0 } }
    dp[0][0] = matrix[0][0]

    for (x in 1 until n) {
        dp[0][x] = matrix[0][x] + dp[0][x - 1]
    }

    for (y in 1 until n) {
        dp[y][0] = matrix[y][0] + dp[y - 1][0]
    }


    for (y in 1 until n) {
        for (x in 1 until n) {
            dp[y][x] = max(dp[y - 1][x] + matrix[y][x], dp[y][x - 1] + matrix[y][x])
        }
    }

    println(dp[n - 1][n - 1])
}